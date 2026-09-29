from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents


PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


documents = load_pdf(PDF_PATH)
chunks = split_documents(documents)

print(f"Total pages: {len(documents)}")
print(f"Total chunks: {len(chunks)}")

for chunk in chunks[:5]:
    print("\n" + "=" * 70)
    print(f"Chunk ID: {chunk.metadata['chunk_id']}")
    print(f"Source: {chunk.metadata['source']}")
    print(f"Page: {chunk.metadata['page']}")
    print(f"Characters: {len(chunk.page_content)}")
    print("Text:")
    print(chunk.page_content[:400])