import { useState } from "react";
import "./App.css";

import UploadCard from "./components/UploadCard";
import AnalysisDashboard from "./components/AnalysisDashboard";
import AnalystChat from "./components/AnalystChat";


function App() {
  const [analysisData, setAnalysisData] = useState(null);
  const [activePage, setActivePage] = useState("dashboard");
  return (
    <div className="app">

      <aside className="sidebar">

        <div className="brand">
          <div className="brand-mark">B</div>
          <span>BriefLens</span>
        </div>

        <nav className="navigation">

          <button
          className={`nav-item ${
            activePage === "dashboard" ? "active" : ""
          }`}
          onClick={() => setActivePage("dashboard")}
        >
          <span>⌂</span>
          Dashboard
        </button>

          <button className="nav-item">
            <span>▣</span>
            Documents
          </button>

          <button className="nav-item">
            <span>◈</span>
            Analysis
          </button>

          <button
          className={`nav-item ${
            activePage === "chat" ? "active" : ""
          }`}
          onClick={() => setActivePage("chat")}
        >
          <span>◌</span>
          Analyst Chat
        </button>

        </nav>

        <div className="sidebar-footer">

          <div className="status-dot"></div>

          <div>
            <strong>System ready</strong>
            <span>BriefLens AI</span>
          </div>

        </div>

      </aside>


      <main className="main-content">

        <header className="topbar">

          <div>
            <span className="eyebrow">
              DOCUMENT INTELLIGENCE
            </span>

            <h1>
              Good evening, Analyst.
            </h1>
          </div>


          <div className="profile">

            <div className="profile-avatar">
              A
            </div>

            <span>
              Analyst
            </span>

          </div>

        </header>


        {activePage === "chat" ? (
            <AnalystChat
              document={analysisData?.fileName}
            />
          ) : analysisData ? (

            <AnalysisDashboard
              analysis={analysisData.analysis}
              onNewAnalysis={() => setAnalysisData(null)}
            />

          ) : (

            <>
              <section className="hero">

                <div className="hero-copy">

                  <span className="hero-label">
                    AI POWERED BRIEF ANALYSIS
                  </span>

                  <h2>
                    Turn client briefs into
                    <span>
                      {" "}actionable intelligence.
                    </span>
                  </h2>

                  <p>
                    Upload a client brief and let BriefLens
                    identify requirements, missing information,
                    risks, and next steps : with evidence linked
                    back to the source.
                  </p>

                </div>

                <UploadCard
                  onAnalysisComplete={setAnalysisData}
                />

              </section>


              <section className="recent-section">

                <div className="section-heading">

                  <div>

                    <span className="eyebrow">
                      WORKSPACE
                    </span>

                    <h2>
                      Recent analyses
                    </h2>

                  </div>

                  <button className="view-all">
                    View all →
                  </button>

                </div>


                <div className="empty-state">

                  <div className="empty-icon">
                    ◫
                  </div>

                  <h3>
                    No analyses yet
                  </h3>

                  <p>
                    Upload your first client brief to see
                    your analysis history here.
                  </p>

                </div>

              </section>

            </>

          )}

      </main>

    </div>
  );
}


export default App;