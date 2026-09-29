from pydantic import BaseModel, Field

from app.analysis.schemas import Evidence


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    question: str
    document: str
    history: list[ChatMessage] = Field(default_factory=list)


class ChatResponse(BaseModel):
    answer: str
    evidence: list[Evidence]