from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store
from app.rag.retriever import retrieve_documents
from app.analysis.analyzer import analyze_brief
from app.analysis.analysis_context import build_analysis_context
from app.analysis.analysis_validator import validate_analysis_evidence


PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


# --------------------------------------------------
# 1. Load PDF
# --------------------------------------------------

documents = load_pdf(PDF_PATH)

print(f"Loaded pages: {len(documents)}")


# --------------------------------------------------
# 2. Create chunks
# --------------------------------------------------

chunks = split_documents(documents)

print(f"Created chunks: {len(chunks)}")


# --------------------------------------------------
# 3. Create vector store
# --------------------------------------------------

vector_store = create_vector_store(chunks)

print("Vector store created successfully.")


# 4. Build complete analysis context
context = build_analysis_context(chunks)

print(f"Analysis context chunks: {len(chunks)}")


# --------------------------------------------------
# 6. Analyze the brief
# --------------------------------------------------
# 5. Analyze the brief using the complete context
analysis = analyze_brief(context)
# 6. Validate and deduplicate evidence
analysis = validate_analysis_evidence(
    analysis=analysis,
    documents=chunks,
)

# --------------------------------------------------
# 7. Display results
# --------------------------------------------------

print("\n" + "=" * 70)
print("BRIEFLENS BRIEF ANALYSIS")
print("=" * 70)


print("\nSUMMARY:")
print(analysis.summary)

print("\nBRIEF INSTRUCTIONS:")

for instruction in analysis.brief_instructions:

    print("\n" + "-" * 70)

    print(f"Title: {instruction.title}")
    print(f"Description: {instruction.description}")

    print("Evidence:")

    for evidence in instruction.evidence:
        print(
            f"  - {evidence.source} | "
            f"Page {evidence.page} | "
            f"{evidence.chunk_id}"
        )
        print(f"    Evidence: {evidence.relevant_text}")


print("\nREQUIREMENTS:")

for requirement in analysis.requirements:

    print("\n" + "-" * 70)

    print(f"Title: {requirement.title}")
    print(f"Description: {requirement.description}")
    print(f"Priority: {requirement.priority}")

    print("Evidence:")

    for evidence in requirement.evidence:
        print(
            f"  - {evidence.source} | "
            f"Page {evidence.page} | "
            f"{evidence.chunk_id}"
        )
        print(f"    Evidence: {evidence.relevant_text}")


print("\nMISSING INFORMATION:")

for item in analysis.missing_information:

    print("\n" + "-" * 70)

    print(f"Item: {item.item}")
    print(f"Reason: {item.reason}")

    print("Evidence:")

    for evidence in item.evidence:
        print(
            f"  - {evidence.source} | "
            f"Page {evidence.page} | "
            f"{evidence.chunk_id}"
        )
        print(f"    Evidence: {evidence.relevant_text}")
        
print("\nRISKS / AMBIGUITIES:")

for risk in analysis.risks:

    print("\n" + "-" * 70)

    print(f"Title: {risk.title}")
    print(f"Description: {risk.description}")
    print(f"Severity: {risk.severity}")

    print("Evidence:")

    for evidence in risk.evidence:
        print(
            f"  - {evidence.source} | "
            f"Page {evidence.page} | "
            f"{evidence.chunk_id}"
        )
        print(f"    Evidence: {evidence.relevant_text}")
        
print("\nRECOMMENDATIONS:")

for recommendation in analysis.recommendations:

    print("\n" + "-" * 70)

    print(f"Title: {recommendation.title}")
    print(f"Description: {recommendation.description}")
    print(f"Action: {recommendation.action}")
    print(f"Related Risk: {recommendation.related_risk}")

    print("Evidence:")

    for evidence in recommendation.evidence:
        print(
            f"  - {evidence.source} | "
            f"Page {evidence.page} | "
            f"{evidence.chunk_id}"
        )
        print(f"    Evidence: {evidence.relevant_text}")