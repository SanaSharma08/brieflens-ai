from app.graph.state import BriefAnalysisState


state: BriefAnalysisState = {
    "file_path": "../uploads/client-brief-extended-pdf.pdf"
}


print("=" * 70)
print("LANGGRAPH STATE TEST")
print("=" * 70)

print("State created successfully.")
print(f"File path: {state['file_path']}")