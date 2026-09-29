from app.analysis.evidence import deduplicate_evidence
from app.analysis.evidence_validator import validate_evidence


def validate_analysis_evidence(
    analysis,
    documents,
):
    """
    Validate and deduplicate evidence across the complete
    BriefAnalysis object.

    Findings without valid evidence are removed.
    """

    sections = [
        analysis.requirements,
        analysis.brief_instructions,
        analysis.missing_information,
        analysis.risks,
        analysis.recommendations,
    ]

    for section in sections:
        valid_items = []

        for item in section:

            valid_evidence = []

            for evidence in item.evidence:
                if validate_evidence(evidence, documents):
                    valid_evidence.append(evidence)

            valid_evidence = deduplicate_evidence(
                valid_evidence
            )

            if valid_evidence:
                item.evidence = valid_evidence
                valid_items.append(item)

        section.clear()
        section.extend(valid_items)

    return analysis