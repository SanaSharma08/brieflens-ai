from typing import TypedDict

from langchain_core.documents import Document

from app.analysis.schemas import BriefAnalysis


class BriefAnalysisState(TypedDict, total=False):
    """
    State shared between nodes in the BriefLens analysis graph.
    """

    file_path: str

    documents: list[Document]

    chunks: list[Document]

    context: str

    analysis: BriefAnalysis