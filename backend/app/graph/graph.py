# This is where we'll finally connect the nodes. 

# START
#   │
#   ▼
# load_documents
#   │
#   ▼
# split_documents
#   │
#   ▼
# build_context
#   │
#   ▼
# analyze_brief
#   │
#   ▼
# validate_analysis
#   │
#   ▼
#  END

from langgraph.graph import StateGraph, START, END

from app.graph.state import BriefAnalysisState
from app.graph.nodes import (
    load_documents_node,
    split_documents_node,
    build_context_node,
    analyze_brief_node,
    validate_analysis_node,
)


def build_analysis_graph():
    """
    Build the complete BriefLens analysis graph.
    """

    graph = StateGraph(BriefAnalysisState)

    graph.add_node(
        "load_documents",
        load_documents_node,
    )

    graph.add_node(
        "split_documents",
        split_documents_node,
    )

    graph.add_node(
        "build_context",
        build_context_node,
    )

    graph.add_node(
        "analyze_brief",
        analyze_brief_node,
    )

    graph.add_node(
        "validate_analysis",
        validate_analysis_node,
    )

    graph.add_edge(
        START,
        "load_documents",
    )

    graph.add_edge(
        "load_documents",
        "split_documents",
    )

    graph.add_edge(
        "split_documents",
        "build_context",
    )

    graph.add_edge(
        "build_context",
        "analyze_brief",
    )

    graph.add_edge(
        "analyze_brief",
        "validate_analysis",
    )

    graph.add_edge(
        "validate_analysis",
        END,
    )

    return graph.compile()