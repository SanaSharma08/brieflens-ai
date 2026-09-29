from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document


def load_pdf(file_path: str) -> list[Document]:
    """
    Load a PDF and return one LangChain Document per page.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    reader = PdfReader(str(path))

    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if not text or not text.strip():
            continue

        document = Document(
            page_content=text.strip(),
            # eg output: This recommendation is based on client-brief-extended-pdf.pdf, page 4.
            # we're preserving metadata before we introduce RAG
            metadata={
                "source": path.name,
                "page": page_number,
            },
        )

        documents.append(document)

    return documents