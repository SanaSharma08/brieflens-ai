from app.llm import get_llm
from app.analysis.schemas import BriefAnalysis


def analyze_brief(context: str) -> BriefAnalysis:
    """
    Analyze retrieved brief context and return a structured
    BriefAnalysis response.
    """

    llm = get_llm()

    structured_llm = llm.with_structured_output(BriefAnalysis)

    prompt = f"""
You are an AI analyst for BriefLens AI.

Analyze the provided client brief context and return a
structured analysis.

IMPORTANT RULES:

1. Use ONLY the provided document context.
2. Do NOT invent client requirements, goals, constraints,
   audiences, or decisions.
3. Carefully distinguish between:
   - actual client requirements
   - instructions about how the briefing/project process works
   - questions or fields that the brief asks the client to fill
   - information that is missing

4. Put actual client requirements in "requirements".

5. Put process instructions, document instructions, or
   general statements about how the web team/client should
   work together in "brief_instructions".

6. If the document is a blank template, do NOT treat the
   template's questions as confirmed client requirements.

7. Identify actual requirements only when the document provides
   enough evidence that they are client-specific.
8. Preserve the exact source, page number, and chunk ID from
   the context.
9. For every evidence item, relevant_text must be copied
    directly from the provided document context.

10. Do NOT paraphrase, summarize, or invent relevant_text.

11. The relevant_text should contain only the smallest
    useful excerpt from the provided context that supports
    the finding.

12. The source, page, and chunk_id of an evidence item must
    correspond to the exact chunk from which relevant_text
    was taken.

13. If the context does not contain sufficient evidence for
    a finding, do not create that finding.
14. Keep descriptions concise and factual.
15. Do not use outside knowledge.
16. Identify genuine risks or ambiguities that could affect
   project planning, development, delivery, or decision-making.

17. A risk must be supported by evidence from the document.
   Do not invent hypothetical risks that are unrelated to
   information present in the brief.

18. Missing information may create a risk, but do not simply
    duplicate every missing-information item as a risk.
    Identify a risk only when the missing or unclear information
    could materially affect the project.

19. For severity, use only:
    - "high"
    - "medium"
    - "low"

20. Every risk must include supporting evidence with the exact
    source, page, and chunk ID.
    
21. For each recommendation, propose a concrete next action
    that the project team can take based only on the identified
    risks or missing information.

22. Recommendations must be actionable rather than generic.
    For example, "clarify requirements" is too vague.
    Prefer specific actions such as "Confirm the target
    delivery deadline with the client before sprint planning."

23. Do not invent project decisions or assume that the client
    has agreed to a particular solution.

24. Each recommendation must identify the related risk and
    include supporting evidence from the document.

For priority:
- Use "high", "medium", or "low".
- Only assign a priority when the document provides enough
  evidence to justify it.
- If priority cannot be established, use "medium" rather than
  inventing a reason.

Document context:

{context}
"""

    response = structured_llm.invoke(prompt)

    return response