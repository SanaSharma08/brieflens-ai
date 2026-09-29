from pathlib import Path

from langchain_chroma import Chroma

from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.embeddings import get_embedding_model
# using one persistent Chroma collection for all documents, so that we can retrieve across multiple documents

BASE_DIR = Path(__file__).resolve().parents[3]
CHROMA_PATH = str(BASE_DIR / "chroma_db")


def index_document(file_path: str) -> Chroma:
    """
    Load, chunk, embed, and store a PDF in Chroma.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    # Load PDF pages
    documents = load_pdf(str(path))

    if not documents:
        raise ValueError(
            "No readable text was found in the PDF."
        )

    # Split pages into chunks
    chunks = split_documents(documents)

    if not chunks:
        raise ValueError(
            "No chunks were created from the PDF."
        )

    # Create embeddings
    embedding_model = get_embedding_model()

    # Open the persistent Chroma collection
    vector_store = Chroma(
        collection_name="brief_documents",
        embedding_function=embedding_model,
        persist_directory=CHROMA_PATH,
    )

    # Check whether this document is already indexed
    existing = vector_store.get(
        where={"source": path.name}
    )

    existing_ids = set(existing.get("ids", []))

    new_chunks = [
        chunk
        for chunk in chunks
        if chunk.metadata["chunk_id"] not in existing_ids
    ]

    if new_chunks:
        vector_store.add_documents(
            documents=new_chunks,
            ids=[
                chunk.metadata["chunk_id"]
                for chunk in new_chunks
            ],
        )

    return vector_store