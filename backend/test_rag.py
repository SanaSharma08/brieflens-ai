from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store
from app.rag.retriever import retrieve_documents
from app.llm import get_llm
from app.schemas import RAGResponse
# This script demonstrates the end-to-end process of loading a PDF document, splitting it into chunks, creating a vector store for retrieval, and using a structured LLM to answer a user's question based on the document's content.

PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


# --------------------------------------------------
# 1. Load and prepare document
# --------------------------------------------------

documents = load_pdf(PDF_PATH)
chunks = split_documents(documents)

print(f"Loaded pages: {len(documents)}")
print(f"Created chunks: {len(chunks)}")


# --------------------------------------------------
# 2. Create vector store
# --------------------------------------------------

vector_store = create_vector_store(chunks)

print("Vector store created successfully.")


# --------------------------------------------------
# 3. Retrieve relevant evidence
# --------------------------------------------------

query = "What are the client's website requirements?"

results = retrieve_documents(
    vector_store=vector_store,
    query=query,
    k=3,
)


# --------------------------------------------------
# 4. Build context
# --------------------------------------------------

context_parts = []

for result in results:
    source = result.metadata["source"]
    page = result.metadata["page"]
    chunk_id = result.metadata["chunk_id"]

    context_parts.append(
        f"""
Source: {source}
Page: {page}
Chunk ID: {chunk_id}

Content:
{result.page_content}
"""
    )

context = "\n\n".join(context_parts)


# --------------------------------------------------
# 5. Create structured LLM
# --------------------------------------------------

llm = get_llm()

structured_llm = llm.with_structured_output(RAGResponse)


# --------------------------------------------------
# 6. Prompt
# --------------------------------------------------

prompt = f"""
You are an AI analyst for BriefLens AI.

Answer the user's question using ONLY the provided document
context.

Important rules:

1. Do not invent information.
2. If the document is a blank template, explicitly say that
   the actual client-specific requirements are not available.
3. Distinguish between information that is actually provided
   and questions/items that the document asks the client to
   provide.
4. Every piece of evidence must come from the provided context.
5. For each evidence item, preserve the exact source, page,
   and chunk ID from the context.

User question:
{query}

Document context:
{context}
"""


# --------------------------------------------------
# 7. Generate response
# --------------------------------------------------

response = structured_llm.invoke(prompt)


# --------------------------------------------------
# 8. Display response
# --------------------------------------------------

print("\n" + "=" * 70)
print("BRIEFLENS STRUCTURED RESPONSE")
print("=" * 70)

print("\nAnswer:")
print(response.answer)

print("\nEvidence:")

for evidence in response.evidence:
    print("\n" + "-" * 70)
    print(f"Source: {evidence.source}")
    print(f"Page: {evidence.page}")
    print(f"Chunk ID: {evidence.chunk_id}")
    print(f"Relevant text: {evidence.relevant_text}")