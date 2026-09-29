from langchain_chroma import Chroma


def retrieve_documents(
    vector_store: Chroma,
    query: str,
    k: int = 3,
    source: str | None = None,
):
    """
    Retrieve relevant document chunks.

    If a source is provided, retrieval is restricted
    to that document.
    """

    search_kwargs = {}

    if source:
        search_kwargs["filter"] = {
            "source": source
        }

    results = vector_store.similarity_search(
        query,
        k=k,
        **search_kwargs,
    )

    return results