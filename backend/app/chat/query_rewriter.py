from app.llm import get_llm


def rewrite_query(
    question: str,
    history: list,
) -> str:
    """
    Rewrite a conversational question into a
    self-contained retrieval query.
    """

    if not history:
        return question

    conversation = "\n".join(
        f"{message.role.upper()}: {message.content}"
        for message in history
    )

    llm = get_llm()

    prompt = f"""
You are a query rewriting component for BriefLens AI.

Your job is to rewrite the user's latest question into a
self-contained search query for retrieving relevant passages
from a client brief.

Use the conversation history only to resolve references such as:
- this
- that
- those
- it
- they
- the previous item
- the second one

Rules:

1. Preserve the user's original intent.
2. Do not answer the question.
3. Do not add information that is not present in the conversation.
4. If the question is already self-contained, return it unchanged.
5. Return ONLY the rewritten search query.
6. Keep the query concise.

CONVERSATION HISTORY:
{conversation}

LATEST USER QUESTION:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip()