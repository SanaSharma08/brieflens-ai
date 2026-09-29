from langchain_chroma import Chroma
from langchain_core.documents import Document
from pathlib import Path
from app.rag.embeddings import get_embedding_model


BASE_DIR = Path(__file__).resolve().parents[3]
CHROMA_PATH = str(BASE_DIR / "chroma_db")
# This module provides functions to create a Chroma vector store from document chunks. It uses the `langchain` library to create a vector store and the `langchain_huggingface` library to get the embedding model.

def create_vector_store(documents: list[Document]) -> Chroma:
    """
    Create a Chroma vector store from document chunks.
    """

    embedding_model = get_embedding_model()

    ids = [
        document.metadata["chunk_id"]
        for document in documents
    ] # note: this is a list of chunk_ids, which are unique identifiers for each document chunk, generated in the split_documents function.
    # each chunk has a stable identity, which is important for the vector store to maintain consistency across runs.

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        ids=ids,
        persist_directory=CHROMA_PATH,
    )

    return vector_store

def get_vector_store() -> Chroma:
    """
    Open the existing persistent Chroma collection.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        collection_name="brief_documents",
        embedding_function=embedding_model,
        persist_directory=CHROMA_PATH,
    )

    return vector_store