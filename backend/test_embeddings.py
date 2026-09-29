from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.embeddings import get_embedding_model


PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


documents = load_pdf(PDF_PATH)
chunks = split_documents(documents)

embedding_model = get_embedding_model()

text = chunks[0].page_content

vector = embedding_model.embed_query(text)

print(f"Text length: {len(text)}")
print(f"Embedding dimensions: {len(vector)}")
print(f"First 10 values: {vector[:10]}")