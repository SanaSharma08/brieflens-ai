from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store
from app.rag.retriever import retrieve_documents

# Testing the entire RAG pipeline: loading a PDF, splitting it into chunks, creating a vector store, and retrieving relevant documents based on a query.
PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


documents = load_pdf(PDF_PATH)
chunks = split_documents(documents)

print(f"Loaded pages: {len(documents)}")
print(f"Created chunks: {len(chunks)}")

vector_store = create_vector_store(chunks)

print("Vector store created successfully.")


query = "What are the client's website requirements?"

results = retrieve_documents(
    vector_store=vector_store,
    query=query,
    k=3,
)


print("\n" + "=" * 70)
print(f"Query: {query}")
print("=" * 70)

for index, result in enumerate(results, start=1):
    print("\n" + "-" * 70)
    print(f"Result {index}")
    print(f"Source: {result.metadata['source']}")
    print(f"Page: {result.metadata['page']}")
    print(f"Chunk ID: {result.metadata['chunk_id']}")
    print("\nText:")
    print(result.page_content[:500])