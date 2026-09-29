from pydantic import BaseModel
# This gives us a contract for what our data should look like

class Evidence(BaseModel):
    source: str
    page: int
    chunk_id: str
    relevant_text: str


class RAGResponse(BaseModel):
    answer: str
    evidence: list[Evidence]