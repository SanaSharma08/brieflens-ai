from app.graph.graph import build_analysis_graph
from app.graph.state import BriefAnalysisState


PDF_PATH = "../uploads/client-brief-extended-pdf.pdf"


graph = build_analysis_graph()

initial_state: BriefAnalysisState = {
    "file_path": PDF_PATH
}

print("=" * 70)
print("BRIEFLENS LANGGRAPH TEST")
print("=" * 70)

result = graph.invoke(initial_state)

print("\nGraph execution completed successfully.")

print("\n" + "=" * 70)
print("FINAL ANALYSIS")
print("=" * 70)

analysis = result["analysis"]

print("\nSummary:")
print(analysis.summary)

print("\nRequirements:")
print(len(analysis.requirements))

print("\nBrief Instructions:")
print(len(analysis.brief_instructions))

print("\nMissing Information:")
print(len(analysis.missing_information))

print("\nRisks:")
print(len(analysis.risks))

print("\nRecommendations:")
print(len(analysis.recommendations))