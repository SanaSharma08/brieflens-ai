from app.analysis.schemas import Evidence

# Used when we already know the exact evidence text:
def create_evidence(
    document,
    relevant_text: str | None = None,
) -> Evidence:
    """
    Convert a LangChain Document into a structured Evidence object.

    If a relevant_text excerpt is provided, use it.
    Otherwise, use the complete chunk text.
    """

    text = relevant_text or document.page_content

    return Evidence(
        source=document.metadata["source"],
        page=document.metadata["page"],
        chunk_id=document.metadata["chunk_id"],
        relevant_text=text.strip(),
    )

# Used when we know a phrase that is relevant:
def create_evidence_excerpt(
    document,
    start_text: str,
    max_length: int = 300,
) -> Evidence:
    """
    Create a short evidence excerpt starting from a relevant phrase.

    The original source, page, and chunk ID are preserved.
    """

    text = document.page_content.strip()

    start_index = text.lower().find(start_text.lower())

    if start_index == -1:
        excerpt = text[:max_length]
    else:
        excerpt = text[start_index:start_index + max_length]

    return create_evidence(
        document=document,
        relevant_text=excerpt,
    )
    
# deduplication 
def deduplicate_evidence(
    evidence_items: list[Evidence],
) -> list[Evidence]:
    """
    Remove duplicate evidence items.

    Two evidence items are considered duplicates when they
    reference the same source, page, chunk, and text.
    """

    unique_items = []
    seen = set()

    for evidence in evidence_items:
        key = (
            evidence.source,
            evidence.page,
            evidence.chunk_id,
            evidence.relevant_text.strip(),
        )

        if key not in seen:
            seen.add(key)
            unique_items.append(evidence)

    return unique_items