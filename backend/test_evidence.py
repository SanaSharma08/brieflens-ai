from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents
from app.analysis.evidence import create_evidence_excerpt
from app.analysis.evidence import deduplicate_evidence


PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


# 1. Load PDF
documents = load_pdf(PDF_PATH)

# 2. Create chunks
chunks = split_documents(documents)

# 3. Find a relevant excerpt
evidence = create_evidence_excerpt(
    document=chunks[2],
    start_text="Project deadline",
)


duplicate_evidence = [
    evidence,
    evidence,
    evidence,
]

unique_evidence = deduplicate_evidence(
    duplicate_evidence
)

print("\n" + "=" * 70)
print("DEDUPLICATION TEST")
print("=" * 70)

print(f"Before: {len(duplicate_evidence)}")
print(f"After: {len(unique_evidence)}")


print("=" * 70)
print("EVIDENCE EXCERPT TEST")
print("=" * 70)

print(f"Source: {evidence.source}")
print(f"Page: {evidence.page}")
print(f"Chunk ID: {evidence.chunk_id}")

print("\nRelevant excerpt:")
print(evidence.relevant_text)