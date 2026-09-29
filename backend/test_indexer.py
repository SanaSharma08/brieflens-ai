from app.rag.indexer import index_document


PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


vector_store = index_document(PDF_PATH)


results = vector_store.similarity_search(
    "What information is missing?",
    k=3,
    filter={"source": "client-brief-extended-pdf.pdf"},
)


print("INDEXING TEST")
print("=" * 60)

print(f"Retrieved chunks: {len(results)}")

for document in results:
    print("\n" + "-" * 60)
    print(
        f"Source: {document.metadata['source']}"
    )
    print(
        f"Page: {document.metadata['page']}"
    )
    print(
        f"Chunk: {document.metadata['chunk_id']}"
    )
    print(
        document.page_content[:300]
    )