from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

from app.analysis.service import analyze_document
from app.analysis.schemas import BriefAnalysis

from app.chat.schemas import ChatRequest, ChatResponse
from app.chat.service import chat_with_document

from app.rag.indexer import index_document


router = APIRouter(
    prefix="/api",
    tags=["Analysis"],
)


BASE_DIR = Path(__file__).resolve().parents[3]
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post(
    "/analyze",
    response_model=BriefAnalysis,
)
async def analyze_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF and analyze it using the BriefLens AI pipeline.
    """

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    file_path = UPLOAD_DIR / file.filename

    contents = await file.read()

    with open(file_path, "wb") as buffer:
        buffer.write(contents)
        
    # Index the document for future retrieval and chat
    index_document(str(file_path))
    
    analysis = analyze_document(str(file_path))

    return analysis

@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):
    """
    Answer a question using document-grounded retrieval.
    """

    file_path = UPLOAD_DIR / request.document

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Document not found.",
        )

    try:
        response = chat_with_document(
        file_path=str(file_path),
        question=request.question,
        history=request.history,
    )

        return response

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )