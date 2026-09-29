from app.graph.graph import build_analysis_graph


def analyze_document(file_path: str):
    """
    Run the complete BriefLens document analysis pipeline
    using the LangGraph workflow.
    """

    graph = build_analysis_graph()

    result = graph.invoke({
        "file_path": file_path,
    })

    return result["analysis"]