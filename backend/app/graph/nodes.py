from app.ingestion.pdf_loader import load_pdf
from app.rag.splitter import split_documents
from app.analysis.analysis_context import build_analysis_context
from app.analysis.analyzer import analyze_brief
from app.analysis.analysis_validator import validate_analysis_evidence
from app.graph.state import BriefAnalysisState


def load_documents_node(
    state: BriefAnalysisState,
) -> BriefAnalysisState:
    """
    Load the PDF specified in the graph state.
    """

    documents = load_pdf(state["file_path"])

    return {
        **state,
        "documents": documents,
    }


def split_documents_node(
    state: BriefAnalysisState,
) -> BriefAnalysisState:
    """
    Split loaded documents into smaller chunks.
    """

    chunks = split_documents(state["documents"])

    return {
        **state,
        "chunks": chunks,
    }
    
def build_context_node(
    state: BriefAnalysisState,
) -> BriefAnalysisState:
    """
    Build the analysis context from document chunks.
    """

    context = build_analysis_context(state["chunks"])

    return {
        **state,
        "context": context,
    }

def analyze_brief_node(
    state: BriefAnalysisState,
) -> BriefAnalysisState:
    """
    Analyze the document context using the LLM.
    """

    analysis = analyze_brief(state["context"])

    return {
        **state,
        "analysis": analysis,
    }
    
def validate_analysis_node(
    state: BriefAnalysisState,
) -> BriefAnalysisState:
    """
    Validate and deduplicate evidence produced by the LLM.
    """

    analysis = validate_analysis_evidence(
        analysis=state["analysis"],
        documents=state["chunks"],
    )

    return {
        **state,
        "analysis": analysis,
    }