# BriefLens AI

**From client briefs to actionable intelligence.**

BriefLens AI is a GenAI-powered document intelligence platform that transforms unstructured client briefs into structured, evidence-backed insights.

Instead of simply summarizing a document, BriefLens analyzes the brief to identify:

- Client requirements
- Brief instructions
- Missing information
- Project risks
- Actionable recommendations
- Source-level evidence

It also provides an **Analyst Chat** interface that allows users to ask contextual questions about an uploaded document and receive grounded responses with page- and chunk-level citations.

---

## 🔴 Live Demo
- Frontend: https://brieflens-ai.vercel.app
- Backend API: https://brieflens-ai.onrender.com
- API Documentation: https://brieflens-ai.onrender.com/docs
---
## Images
<img width="1900" height="934" alt="{54955778-8C17-41B6-9D7F-72EC5CB4415A}" src="https://github.com/user-attachments/assets/2759ea95-4bf2-4e88-acce-fcbd2122605d" />
<img width="1819" height="932" alt="{D636069F-95B3-46FF-B111-D1DE6DBA31C6}" src="https://github.com/user-attachments/assets/8eba1217-9e9d-4eb9-a3d5-99a32d2c5719" />
<img width="1853" height="899" alt="{25BFB6B6-EB7A-4FC7-85CF-02F601E8584D}" src="https://github.com/user-attachments/assets/55988a45-fcdf-4d88-bf5b-cff638242877" />
<img width="1842" height="868" alt="{969E6D28-F532-4E06-B2F0-D98DC5C68CA9}" src="https://github.com/user-attachments/assets/8a8f2fbe-64c5-43a3-9e22-2d267897bb6d" />
<img width="1810" height="859" alt="{A601209C-A999-41C4-A1CC-99128C50BE4F}" src="https://github.com/user-attachments/assets/cbf4482b-1699-40a3-96a6-ba1cf55b0a61" />
<img width="1844" height="927" alt="{5153AA50-4114-4253-9AA8-92011A60383E}" src="https://github.com/user-attachments/assets/c1dcf348-f0d9-46b1-8f47-c81f54d4b0e2" />


---
## Why BriefLens AI?

Client briefs often contain much more than clearly defined requirements.

A typical brief can mix:

- Actual requirements
- Questions the client is expected to answer
- Optional features
- Design preferences
- Process instructions
- Missing project information
- Technical constraints
- Business expectations
- References and examples

This creates a common problem:

 **Before development begins, someone still has to turn a document into an actionable understanding of what actually needs to be built.**

A simple document summarizer does not solve this problem.

For example, if a template says:

 "Optimisation for mobile phones"

that does not necessarily mean the client explicitly requested mobile optimization.

Similarly, a template may contain a list of possible features without indicating which ones the client actually selected.

BriefLens was designed around this distinction.

The system attempts to separate **what the document says** from **what can safely be concluded from it**.

---

# The Development Journey

BriefLens AI was built around a simple progression:

```text
Unstructured Client Brief
          ↓
     PDF Extraction
          ↓
        Chunking
          ↓
      Embeddings
          ↓
    Vector Storage
          ↓
   Grounded Retrieval
          ↓
     AI Analysis
          ↓
 Evidence Validation
          ↓
Structured Intelligence
          ↓
 Conversational Analyst
```
The project evolved from a basic PDF-processing workflow into a complete full-stack GenAI application.

# Core Features
## 1. PDF Document Analysis

Users can upload a client brief directly through the web interface.

The backend:

Receives the PDF
Extracts page-level text
Creates structured document objects
Splits the document into manageable chunks
Preserves source metadata
Runs the analysis workflow

Each chunk retains information such as:

Source
Page
Chunk ID
Text

This metadata becomes important later when generating evidence.

## 2. Requirement Extraction

BriefLens identifies requirements that can be supported by the document.

Each requirement contains:

Title
Description
Priority
Evidence

The system is instructed not to treat every feature mentioned in a template as a confirmed client requirement.

## 3. Brief Instructions

Not every instruction in a document represents a product requirement.

BriefLens therefore maintains a separate category for instructions such as:

Information the client needs to provide
Questions in a briefing template
Process-related instructions
Documentation guidance

This separation helps prevent template language from being incorrectly interpreted as a confirmed requirement.

## 4. Missing Information Detection

A brief may describe a project without providing enough information to begin development.

BriefLens identifies gaps such as:
```text
Missing Information
        ↓
Why it matters
        ↓
Evidence from the document
```
This makes the analysis useful before a project enters development.

## 5. Risk Identification

The system identifies potential risks supported by the source document.

Each risk contains:

Title
Description
Severity
Evidence

Severity is constrained to:

High
Medium
Low

The model is explicitly instructed not to invent risks that cannot be supported by the supplied document.

## 6. Actionable Recommendations

BriefLens converts identified gaps and risks into recommended actions.

Each recommendation contains:

Title
Description
Action
Related Risk
Evidence

The goal is to move from:

"What does the brief say?"

to:

"What should the team do next?"

## Analyst Chat

The platform also includes a conversational analyst interface.

Instead of repeatedly reading the entire document, users can ask questions such as:

What features are listed?

Which of those are related to mobile users?

Which information would we need from the client before development starts?

The chat system maintains conversation history and uses it to resolve contextual references.
```text
For example:

User:
What features are listed?

Assistant:
[feature information]

User:
Which of those are related to mobile users?
```
The second question is rewritten into a self-contained retrieval query before searching the document.

## Grounded AI

A major design goal of BriefLens is traceability.

An AI-generated answer should not simply sound plausible.

It should be possible to ask:

Where did this information come from?

Every supported finding can therefore contain:

Source document
Page
Chunk ID
Relevant source text
```text
Example:

Source:
client-brief-sample-pdf.pdf

Page:
4

Chunk:
client-brief-sample-pdf.pdf-p4-c1

Evidence:
"Optimisation for mobile phones..."
```
## Evidence Validation

LLMs can generate convincing but unsupported information.

BriefLens therefore does not blindly trust the structured output returned by the model.

The validation pipeline checks whether generated evidence actually exists in the retrieved source content.

Conceptually:
```text
LLM Output
    ↓
Evidence
    ↓
Does source + page + chunk exist?
    ↓
Does relevant_text exist inside the source chunk?
    ↓
      YES
       ↓
Keep finding

      NO
       ↓
Remove unsupported finding
```
This creates an additional verification layer between the model and the user interface.

## Architecture
```text
                         ┌──────────────────────┐
                         │      React + Vite    │
                         │    Vercel Frontend   │
                         └──────────┬───────────┘
                                    │
                                    │ HTTPS
                                    ▼
                         ┌──────────────────────┐
                         │       FastAPI        │
                         │   Render Backend     │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
          ┌────────────┐     ┌──────────────┐   ┌─────────────┐
          │ PDF Loader │     │  LangGraph   │   │   Analyst   │
          │   pypdf    │     │   Workflow   │   │    Chat     │
          └─────┬──────┘     └──────┬───────┘   └──────┬──────┘
                │                   │                  │
                ▼                   ▼                  ▼
          ┌────────────┐     ┌──────────────┐   ┌─────────────┐
          │ Chunking   │     │ Structured   │   │  Retriever  │
          │ LangChain  │     │   Analysis   │   │  ChromaDB   │
          └─────┬──────┘     └──────┬───────┘   └──────┬──────┘
                │                   │                  │
                └──────────┬────────┴──────────────────┘
                           ▼
                    ┌──────────────┐
                    │ OpenAI APIs  │
                    │ LLM + Embed. │
                    └──────────────┘
```
## Analysis Workflow
```text
The document analysis workflow is orchestrated using LangGraph.

START
  │
  ▼
Load Documents
  │
  ▼
Split Documents
  │
  ▼
Build Analysis Context
  │
  ▼
Analyze Brief
  │
  ▼
Validate Evidence
  │
  ▼
END
```
## Why LangGraph?

The analysis process consists of multiple explicit stages.

Instead of hiding the entire workflow inside one large function, LangGraph provides a stateful workflow where each stage has a defined responsibility.

The workflow state contains information such as:

file_path
documents
chunks
context
analysis

This makes the system easier to extend with additional analysis or validation stages.

## RAG Architecture

The conversational system uses a Retrieval-Augmented Generation architecture.
```text
User Question
      ↓
Conversation History
      ↓
Query Rewriting
      ↓
Vector Retrieval
      ↓
Document Filtering
      ↓
Relevant Chunks
      ↓
Grounded LLM
      ↓
Evidence Validation
      ↓
Answer + Citations
```
## Query Rewriting

Conversational questions often depend on previous messages.

For example:

"What features are listed?"

"Which of those are related to mobile users?"

The second query is not completely self-contained.

The query rewriting component uses conversation history to transform it into a retrieval-friendly query.

The rewriting model is explicitly instructed to:

Preserve the original intent
Resolve contextual references
Avoid answering the question
Avoid adding new information
Return only the rewritten query

This improves retrieval for multi-turn conversations.

## Document-Level Retrieval

When chatting with a document, retrieval is filtered by the uploaded document's filename.

Conceptually:
```text
User Question
      ↓
Embedding Search
      ↓
Filter:
source = requested document
      ↓
Top-k relevant chunks
```
This prevents the analyst chat from accidentally retrieving information belonging to another indexed document.

## Structured AI Output

Instead of asking the LLM to return arbitrary JSON, BriefLens uses Pydantic models to define the expected structure.

The analysis schema contains:
```text
BriefAnalysis
├── summary
├── requirements[]
├── brief_instructions[]
├── missing_information[]
├── risks[]
└── recommendations[]
```
Each section contains its own evidence objects.

This makes the AI output predictable and easier for both the backend and frontend to consume.

## Example Data Structure

A simplified finding looks like:
```text
{
  "title": "Mobile optimisation",
  "description": "The brief contains mobile-related requirements.",
  "priority": "medium",
  "evidence": [
    {
      "source": "client-brief.pdf",
      "page": 4,
      "chunk_id": "client-brief.pdf-p4-c1",
      "relevant_text": "Optimisation for mobile phones"
    }
  ]
}

The exact output depends on the source document.
```
## Technology Stack
```text
Frontend
├── React
├── Vite
└── CSS

Backend
├── Python
├── FastAPI
└── Uvicorn

GenAI
├── OpenAI API
├── LangChain
├── LangGraph
└── RAG

Document Processing
└── pypdf

Vector Search
└── ChromaDB

Data Validation
└── Pydantic

Configuration
└── python-dotenv

Deployment
├── Vercel
└── Render
Project Structure
brieflens_ai/
│
├── backend/
│   ├── app/
│   │   │
│   │   ├── analysis/
│   │   │   ├── analysis_context.py
│   │   │   ├── analysis_validator.py
│   │   │   ├── analyzer.py
│   │   │   ├── evidence.py
│   │   │   ├── evidence_validator.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   │
│   │   ├── api/
│   │   │   └── routes.py
│   │   │
│   │   ├── chat/
│   │   │   ├── query_rewriter.py
│   │   │   ├── schemas.py
│   │   │   └── service.py
│   │   │
│   │   ├── graph/
│   │   │   ├── graph.py
│   │   │   ├── nodes.py
│   │   │   └── state.py
│   │   │
│   │   ├── ingestion/
│   │   │   └── pdf_loader.py
│   │   │
│   │   ├── rag/
│   │   │   ├── embeddings.py
│   │   │   ├── indexer.py
│   │   │   ├── retriever.py
│   │   │   ├── splitter.py
│   │   │   └── vector_store.py
│   │   │
│   │   ├── llm.py
│   │   ├── main.py
│   │   └── schemas.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AnalystChat.jsx
│   │   │   ├── AnalysisDashboard.jsx
│   │   │   └── UploadCard.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── .python-version
└── README.md
API
Health Check
GET /

Response:

{
  "message": "BriefLens AI backend is running!"
}
Analyze Document
POST /api/analyze
Request

Multipart form upload:

file: document.pdf
Response

Structured BriefAnalysis object containing:

summary
requirements
brief_instructions
missing_information
risks
recommendations
Analyst Chat
POST /api/chat
Request
{
  "question": "Which features are related to mobile users?",
  "document": "client-brief.pdf",
  "history": [
    {
      "role": "user",
      "content": "What features are listed?"
    },
    {
      "role": "assistant",
      "content": "..."
    }
  ]
}
Response
{
  "answer": "...",
  "evidence": [
    {
      "source": "client-brief.pdf",
      "page": 4,
      "chunk_id": "client-brief.pdf-p4-c1",
      "relevant_text": "..."
    }
  ]
}
```
# Local Development Prerequisites

## Install:

Python 3.13
Node.js
npm
Git

## An OpenAI API key is also required.

## Clone the Repository
git clone https://github.com/SanaSharma08/brieflens-ai.git
cd brieflens-ai
## Backend Setup

Move into the backend directory:

cd backend

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt
Environment Variables

## Create:

.env

in the project root.

## Add:

OPENAI_API_KEY=your_openai_api_key

- Start the Backend
```text  
From:

backend/

run:

python -m uvicorn app.main:app --reload
```
- The API will be available at: http://127.0.0.1:8000
- Swagger documentation: http://127.0.0.1:8000/docs
## Frontend Setup
```text
Open another terminal:

cd frontend

Install dependencies:

npm install
```
Create:

frontend/.env

Add:

VITE_API_BASE_URL=http://127.0.0.1:8000

Start the development server:

npm run dev

Vite will provide a local URL such as:

http://localhost:5173
Production Configuration

The deployed frontend uses:

VITE_API_BASE_URL=[render backend url]

The production architecture is:
```text
Vercel
   │
   │ HTTPS
   ▼
Render
   │
   ├── FastAPI
   ├── LangGraph
   ├── RAG
   ├── ChromaDB
   └── OpenAI API
Deployment
Backend
```
- The backend is deployed on Render.
- The frontend is deployed on Vercel.

## Future ingestion can include:
1. Document Compatibility
DOCX
CSV
TXT
2. Filesystem-based storage

The current V1 stores uploaded files and Chroma data on the service filesystem.

This is suitable for the current demonstration architecture but is not designed as a durable production storage layer.

## A future version can introduce:
```text
Object Storage
      +
Managed Vector Database
      +
Metadata Database
```
3. Single-document workflow

The current user flow focuses on analyzing an uploaded brief and subsequently chatting with that document.

A future workspace model could support:
```text
Workspace
 ├── Client Brief
 ├── Feedback
 ├── Previous Versions
 ├── Design References
 ├── Meeting Notes
 └── Analysis History
```
4. No authentication yet

The current V1 does not implement user authentication or multi-user workspaces.

## Future Roadmap
Phase 2 — Better Document Intelligence
- DOCX ingestion
-CSV ingestion
- Multi-document analysis
- Document version comparison
- Feedback-vs-brief comparison
- Requirement traceability
- Requirement conflict detection
- Phase 3 — Advanced Analysis
- BriefLens can eventually translate a brief into development-oriented artifacts:
```text
Client Brief
     ↓
Requirements
     ↓
User Stories
     ↓
Tasks
     ↓
Dependencies
     ↓
Sprint Breakdown
     ↓
Architecture Suggestions
```
Phase 5 — Team Workspace

A future version could support:

- User accounts
- Client workspaces
- Document history
- Team collaboration
- Saved analyses
- Comments
- Review workflows
- Approval states
- Exportable reports
- Design Principles

## BriefLens AI was built around a few core principles.

1. Ground before generating

AI should retrieve relevant information before generating an answer.

2. Evidence over confidence

A confident response is not necessarily a reliable response.

The system therefore validates evidence against retrieved document content.

3. Separate document facts from interpretation

A template option should not automatically become a confirmed requirement.

BriefLens AI combines several areas of modern software engineering:
```text
Full-Stack Development
React
+
FastAPI
+
REST APIs
+
Vercel
+
Render
Generative AI
OpenAI
+
LangChain
+
Structured Outputs
RAG
Document ingestion
+
Chunking
+
Embeddings
+
Vector search
+
Context retrieval
Agentic / Workflow Architecture
LangGraph
+
Explicit workflow states
+
Modular processing nodes
AI Reliability
Evidence
+
Source metadata
+
Validation
+
Grounding rules
Production Engineering
Environment variables
+
CORS
+
Deployment constraints
+
Memory optimization
+
Production API configuration
V1 Architecture Summary

The current system can be summarized as:

                  BRIEFLENS AI
                       │
              ┌────────┴────────┐
              │                 │
          ANALYSIS            CHAT
              │                 │
              ▼                 ▼
         PDF Loader       Query Rewriter
              │                 │
              ▼                 ▼
          Chunking          Retrieval
              │                 │
              ▼                 ▼
      Analysis Context    Relevant Chunks
              │                 │
              ▼                 ▼
          LangGraph          LLM
              │                 │
              ▼                 ▼
        Structured Output   Chat Response
              │                 │
              └────────┬────────┘
                       ▼
                Evidence Validation
                       │
                       ▼
                React Dashboard
Final Outcome
```

## Tech Stack
["Python", "FastAPI", "React", "Vite", "LangChain", "LangGraph", "OpenAI API", "ChromaDB", "RAG", "Pydantic", "pypdf", "Uvicorn", "Vercel", "Render"]
