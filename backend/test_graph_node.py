from app.graph.state import BriefAnalysisState
from app.graph.nodes import (
    load_documents_node,
    split_documents_node,
    build_context_node,
    analyze_brief_node,
    validate_analysis_node,
)


state: BriefAnalysisState = {
    "file_path": "../uploads/client-brief-extended-pdf.pdf"
}

state = load_documents_node(state)

print("=" * 70)
print("LANGGRAPH ANALYSIS NODE TEST")
print("=" * 70)

print(f"Documents loaded: {len(state['documents'])}")

state = split_documents_node(state)

print(f"Chunks created: {len(state['chunks'])}")

state = build_context_node(state)

print(f"Context created: {bool(state['context'])}")
print(f"Context length: {len(state['context'])} characters")

print("\nRunning LLM analysis...")

state = analyze_brief_node(state)

print("Analysis completed successfully.")

state = validate_analysis_node(state)

print("Evidence validation completed successfully.")

print("\n" + "=" * 70)
print("ANALYSIS RESULT")
print("=" * 70)

print("\nSummary:")
print(state["analysis"].summary)

print("\nRequirements:")
print(len(state["analysis"].requirements))

print("\nBrief Instructions:")
print(len(state["analysis"].brief_instructions))

print("\nMissing Information:")
print(len(state["analysis"].missing_information))

print("\nRisks:")
print(len(state["analysis"].risks))

print("\nRecommendations:")
print(len(state["analysis"].recommendations))