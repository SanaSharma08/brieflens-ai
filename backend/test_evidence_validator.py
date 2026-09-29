from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents
from app.analysis.evidence import create_evidence_excerpt
from app.analysis.evidence_validator import validate_evidence


PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


documents = load_pdf(PDF_PATH)
chunks = split_documents(documents)


# Create valid evidence
valid_evidence = create_evidence_excerpt(
    document=chunks[2],
    start_text="Project deadline",
)


print("=" * 70)
print("VALID EVIDENCE TEST")
print("=" * 70)

print(
    "Validation result:",
    validate_evidence(valid_evidence, chunks)
)


# Create intentionally invalid evidence
invalid_evidence = valid_evidence.model_copy(
    update={
        "relevant_text": "This sentence does not exist in the PDF."
    }
)


print("\n" + "=" * 70)
print("INVALID EVIDENCE TEST")
print("=" * 70)

print(
    "Validation result:",
    validate_evidence(invalid_evidence, chunks)
)