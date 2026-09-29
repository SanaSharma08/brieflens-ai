from app.ingestion.pdf_loader import load_pdf
# Testing extraction of text from a PDF file using the load_pdf function.

PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


documents = load_pdf(PDF_PATH)

print(f"Total pages extracted: {len(documents)}")

for document in documents[:3]:
    print("\n" + "=" * 60)
    print(f"Source: {document.metadata['source']}")
    print(f"Page: {document.metadata['page']}")
    print("Text:")
    print(document.page_content[:500])