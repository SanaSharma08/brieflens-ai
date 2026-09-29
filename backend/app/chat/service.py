from pathlib import Path

from app.rag.vector_store import get_vector_store
from app.rag.retriever import retrieve_documents
from app.llm import get_llm

from app.chat.schemas import ChatResponse
from app.chat.query_rewriter import rewrite_query

from app.analysis.evidence import deduplicate_evidence
from app.analysis.evidence_validator import validate_evidence


def chat_with_document(
    file_path: str,
    question: str,
    history: list,
) -> ChatResponse:
    """
    Answer a question using relevant chunks from the document.
    """

    # 1. Open the existing persistent vector store
    vector_store = get_vector_store()

    # 2. Retrieve only from the requested document
    document_name = Path(file_path).name

    retrieval_query = rewrite_query(
        question=question,
        history=history,
    )

    retrieved_documents = retrieve_documents(
        vector_store=vector_store,
        query=retrieval_query,
        k=4,
        source=document_name,
    )

    if not retrieved_documents:
        return ChatResponse(
            answer=(
                "I could not find enough information in "
                "the provided document to answer this question."
            ),
            evidence=[],
        )

    # 5. Build grounded context
    context_parts = []

    for document in retrieved_documents:
        context_parts.append(
            f"""
SOURCE: {document.metadata["source"]}
PAGE: {document.metadata["page"]}
CHUNK_ID: {document.metadata["chunk_id"]}

TEXT:
{document.page_content}
"""
        )

    context = "\n".join(context_parts)

    # 6. Ask the LLM
    llm = get_llm()

    structured_llm = llm.with_structured_output(
        ChatResponse
    )

    prompt = f"""
You are the analyst assistant for BriefLens AI.

Your job is to answer questions about a client brief
using ONLY the provided document context.

GROUNDING RULES:

1. Use only information present in the provided context.

2. Do not use outside knowledge or assumptions.

3. Carefully distinguish between:
   - confirmed client requirements
   - questions or fields that the client is expected to fill in
   - selectable options listed in a template
   - instructions about completing the brief
   - missing information
   - general process guidance

4. A question, checkbox, selectable option, or example in a
   blank template must NOT be presented as a confirmed client
   requirement unless the document clearly shows that the
   client selected or requested it.

5. If the document is an unfilled template, explicitly state
   that confirmed client-specific requirements cannot be
   determined from the document.

6. When the document contains only a list of possible features,
   describe them as "listed options" or "features the brief
   asks the client to consider", not as requested features.

7. If the document does not contain enough information to answer
   the question, clearly say that the answer is not supported by
   the document.

EVIDENCE RULES:

Every factual answer must include evidence from the provided
context.

For each evidence item:
- source must exactly match the source provided
- page must exactly match the page provided
- chunk_id must exactly match the chunk ID provided
- relevant_text must be copied directly from the provided chunk
- do not paraphrase relevant_text
- do not invent evidence

CONVERSATION HISTORY:
{chr(10).join(
    f"{message.role.upper()}: {message.content}"
    for message in history
)}

USER QUESTION:
{question}

DOCUMENT CONTEXT:
{context}
"""
    response = structured_llm.invoke(prompt)

    # Validate every evidence item against the
    # chunks that were actually retrieved.
    valid_evidence = []

    for evidence in response.evidence:
        if validate_evidence(
            evidence=evidence,
            documents=retrieved_documents,
        ):
            valid_evidence.append(evidence)

    # Remove duplicate evidence items.
    valid_evidence = deduplicate_evidence(
        valid_evidence
    )

    # If the model produced evidence that could not
    # be verified, do not return unsupported evidence.
    if not valid_evidence:
        return ChatResponse(
            answer=(
                "I could not verify enough evidence in "
                "the retrieved document content to answer "
                "this question reliably."
            ),
            evidence=[],
        )

    response.evidence = valid_evidence

    return response