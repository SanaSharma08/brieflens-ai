from pydantic import BaseModel


# BriefAnalysis
# │
# ├── summary
# │
# ├── requirements
# │
# ├── brief_instructions
# │
# └── missing_information

class Evidence(BaseModel):
    source: str
    page: int
    chunk_id: str
    relevant_text: str


class Requirement(BaseModel):
    title: str
    description: str
    priority: str
    evidence: list[Evidence]


class BriefInstruction(BaseModel):
    title: str
    description: str
    evidence: list[Evidence]


class MissingInformation(BaseModel):
    item: str
    reason: str
    evidence: list[Evidence]


class Risk(BaseModel):
    title: str
    description: str
    severity: str
    evidence: list[Evidence]
    
class Recommendation(BaseModel):
    title: str
    description: str
    action: str
    related_risk: str
    evidence: list[Evidence]

class BriefAnalysis(BaseModel):
    summary: str
    requirements: list[Requirement]
    brief_instructions: list[BriefInstruction]
    missing_information: list[MissingInformation]
    risks: list[Risk]
    recommendations: list[Recommendation]