import { useState } from "react";

function AnalysisDashboard({ analysis, onNewAnalysis }) {
  return (
    <section className="analysis-dashboard">
      <div className="analysis-header">
        <div>
          <span className="eyebrow">DOCUMENT ANALYSIS</span>

          <h2>Analysis results</h2>

          <p>
            Structured findings generated from your client brief.
          </p>
        </div>

        <button
          className="new-analysis-button"
          onClick={onNewAnalysis}
        >
          + New analysis
        </button>
      </div>

      <div className="analysis-stats">
        <StatCard
          label="Requirements"
          value={analysis.requirements.length}
        />

        <StatCard
          label="Missing information"
          value={analysis.missing_information.length}
        />

        <StatCard
          label="Risks"
          value={analysis.risks.length}
        />

        <StatCard
          label="Recommendations"
          value={analysis.recommendations.length}
        />
      </div>

      <AnalysisSection
        title="Summary"
        emptyMessage="No summary was generated."
      >
        <div className="summary-card">
          <p>{analysis.summary}</p>
        </div>
      </AnalysisSection>

      <AnalysisSection
        title="Requirements"
        count={analysis.requirements.length}
        emptyMessage="No client-specific requirements were identified."
      >
        {analysis.requirements.map((item, index) => (
          <FindingCard
            key={index}
            title={item.title}
            description={item.description}
            meta={`Priority · ${item.priority}`}
            metaClass={`priority-${item.priority.toLowerCase()}`}
            evidence={item.evidence}
            />
        ))}
      </AnalysisSection>

      <AnalysisSection
        title="Brief Instructions"
        count={analysis.brief_instructions.length}
        emptyMessage="No brief instructions were identified."
        >
        {analysis.brief_instructions.map((item, index) => (
            <FindingCard
            key={index}
            title={item.title}
            description={item.description}
            evidence={item.evidence}
            />
        ))}
        </AnalysisSection>

      <AnalysisSection
        title="Missing Information"
        count={analysis.missing_information.length}
        emptyMessage="No missing information was identified."
      >
        {analysis.missing_information.map((item, index) => (
          <FindingCard
            key={index}
            title={item.item}
            description={item.reason}
            evidence={item.evidence}
          />
        ))}
      </AnalysisSection>

      <AnalysisSection
        title="Risks"
        count={analysis.risks.length}
        emptyMessage="No risks were identified."
      >
        {analysis.risks.map((item, index) => (
          <FindingCard
            key={index}
            title={item.title}
            description={item.description}
            meta={`Severity · ${item.severity}`}
            metaClass={`severity-${item.severity.toLowerCase()}`}
            evidence={item.evidence}
            />
        ))}
      </AnalysisSection>

      <AnalysisSection
        title="Recommendations"
        count={analysis.recommendations.length}
        emptyMessage="No recommendations were generated."
      >
        {analysis.recommendations.map((item, index) => (
          <FindingCard
            key={index}
            title={item.title}
            description={item.description}
            meta={item.action}
            evidence={item.evidence}
          />
        ))}
      </AnalysisSection>
    </section>
  );
}


function StatCard({ label, value }) {
  return (
    <div className="stat-card">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}


function AnalysisSection({
  title,
  count,
  emptyMessage,
  children,
}) {
  return (
    <section className="analysis-section">
      <div className="analysis-section-heading">
        <div>
          <span className="eyebrow">FINDINGS</span>

          <h3>
            {title}

            {count !== undefined && (
              <span className="section-count">
                {count}
              </span>
            )}
          </h3>
        </div>
      </div>

      {children || (
        <div className="analysis-empty">
          {emptyMessage}
        </div>
      )}
    </section>
  );
}


function FindingCard({
  title,
  description,
  meta,
  metaClass,
  evidence,
}) {
  return (
    <article className="finding-card">
      <div className="finding-content">
        <h4>{title}</h4>

        <p>{description}</p>

        {meta && (
          <span className={`finding-meta ${metaClass || ""}`}>
            {meta}
          </span>
        )}
      </div>

      <EvidenceList evidence={evidence} />
    </article>
  );
}


function EvidenceList({ evidence }) {
  const [isExpanded, setIsExpanded] = useState(false);

  if (!evidence || evidence.length === 0) {
    return null;
  }

  return (
    <div className="evidence-container">
      <button
        className="evidence-toggle"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <span>
          {isExpanded
            ? "Hide evidence"
            : "View evidence"}
        </span>

        <span className="evidence-toggle-arrow">
          {isExpanded ? "↑" : "↓"}
        </span>
      </button>

      {isExpanded && (
        <div className="evidence-list">
          <span className="evidence-label">
            SOURCE EVIDENCE
          </span>

          {evidence.map((item, index) => (
            <div
              className="evidence-item"
              key={index}
            >
              <div className="evidence-meta">
                <span>{item.source}</span>

                <span>
                  Page {item.page}
                </span>
              </div>

              <p>
                "{item.relevant_text}"
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}


export default AnalysisDashboard;