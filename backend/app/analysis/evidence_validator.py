from app.analysis.schemas import Evidence


def validate_evidence(
    evidence: Evidence,
    documents: list,
) -> bool:
    """
    Validate that an evidence excerpt actually exists
    in the referenced document chunk.
    """

    for document in documents:
        if (
            document.metadata.get("source") == evidence.source
            and document.metadata.get("page") == evidence.page
            and document.metadata.get("chunk_id") == evidence.chunk_id
        ):
            source_text = document.page_content.strip()
            evidence_text = evidence.relevant_text.strip()

            return evidence_text in source_text

    return False