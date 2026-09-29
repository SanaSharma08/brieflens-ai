from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
# This module provides functions to load and split PDF documents into smaller chunks while preserving metadata. It uses the `pypdf` library to read PDF files and the `langchain` library to create document objects.
# split_documents() automatically carries the original metadata forward.

def split_documents(documents: list[Document]) -> list[Document]:
    """
    Split documents into smaller chunks while preserving metadata.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )

    chunks = text_splitter.split_documents(documents)

    for index, chunk in enumerate(chunks, start=1):
        source = chunk.metadata["source"]
        page = chunk.metadata["page"]

        chunk.metadata["chunk_id"] = (
            f"{source}-p{page}-c{index}"
        )

    return chunks