from app.analysis.service import analyze_document


PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


analysis = analyze_document(PDF_PATH)


print("=" * 70)
print("BRIEFLENS ANALYSIS SERVICE TEST")
print("=" * 70)

print("\nSUMMARY:")
print(analysis.summary)

print("\nREQUIREMENTS:")
print(f"Total: {len(analysis.requirements)}")

print("\nBRIEF INSTRUCTIONS:")
print(f"Total: {len(analysis.brief_instructions)}")

print("\nMISSING INFORMATION:")
print(f"Total: {len(analysis.missing_information)}")

print("\nRISKS:")
print(f"Total: {len(analysis.risks)}")

print("\nRECOMMENDATIONS:")
print(f"Total: {len(analysis.recommendations)}")