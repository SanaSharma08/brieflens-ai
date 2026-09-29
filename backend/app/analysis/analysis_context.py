from langchain_core.documents import Document


def build_analysis_context(
    chunks: list[Document],
) -> str:
    """
    Build a complete context for full-document analysis.

    Unlike normal RAG chat retrieval, this function includes
    all available chunks so important sections of the brief
    are not missed.
    """

    # Remove duplicate chunks using chunk_id
    unique_chunks = {}

    for chunk in chunks:
        chunk_id = chunk.metadata["chunk_id"]

        if chunk_id not in unique_chunks:
            unique_chunks[chunk_id] = chunk

    # Sort chunks by page number and chunk ID
    sorted_chunks = sorted(
        unique_chunks.values(),
        key=lambda chunk: (
            chunk.metadata["page"],
            chunk.metadata["chunk_id"],
        ),
    )

    context_parts = []

    for chunk in sorted_chunks:
        source = chunk.metadata["source"]
        page = chunk.metadata["page"]
        chunk_id = chunk.metadata["chunk_id"]

        context_parts.append(
            f"""
Source: {source}
Page: {page}
Chunk ID: {chunk_id}

Content:
{chunk.page_content}
"""
        )

    return "\n\n".join(context_parts)