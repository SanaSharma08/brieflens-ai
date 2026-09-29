import { useState } from "react";


function AnalystChat({ document }) {
  const [messages, setMessages] = useState([]);

  const [input, setInput] = useState("");

  const [isLoading, setIsLoading] = useState(false);

  const [error, setError] = useState("");


  const handleSubmit = async (event) => {
    event.preventDefault();

    const question = input.trim();

    if (!question || isLoading) {
      return;
    }

    setError("");

    setMessages((previousMessages) => [
      ...previousMessages,
      {
        role: "user",
        content: question,
      },
    ]);

    setInput("");
    setIsLoading(true);

    try {
      const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/api/chat`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: question,
            document: document,
            history: messages.map((message) => ({
                role: message.role,
                content: message.content,
            })),
            }),
        }
      );

      if (!response.ok) {
        const errorData = await response.json();

        throw new Error(
          errorData.detail || "Chat request failed."
        );
      }

      const data = await response.json();

      setMessages((previousMessages) => [
        ...previousMessages,
        {
          role: "assistant",
          content: data.answer,
          evidence: data.evidence,
        },
      ]);
    } catch (error) {
      console.error("Chat error:", error);

      setError(
        error.message ||
        "Something went wrong while asking the document."
      );
    } finally {
      setIsLoading(false);
    }
  };


  return (
    <section className="chat-page">

      <div className="chat-header">

        <div>
          <span className="eyebrow">
            DOCUMENT INTELLIGENCE
          </span>

          <h2>
            Analyst Chat
          </h2>

          <p>
            Ask questions about your client brief
            and get answers grounded in source evidence.
          </p>

          {document && (
            <span className="chat-document">
              Current document · {document}
            </span>
          )}
        </div>

      </div>


      <div className="chat-container">

        {messages.length === 0 ? (

          <div className="chat-empty">

            <div className="chat-empty-icon">
              ✦
            </div>

            <h3>
              Ask your brief anything
            </h3>

            <p>
              Ask about requirements, risks, missing
              information, or anything else contained
              in the document.
            </p>

            <div className="suggested-questions">

              <button
                onClick={() =>
                  setInput(
                    "What are the key requirements in this brief?"
                  )
                }
              >
                What are the key requirements?
              </button>

              <button
                onClick={() =>
                  setInput(
                    "What information is missing from this brief?"
                  )
                }
              >
                What information is missing?
              </button>

              <button
                onClick={() =>
                  setInput(
                    "What are the main risks identified in the brief?"
                  )
                }
              >
                What are the main risks?
              </button>

            </div>

          </div>

        ) : (

          <div className="chat-messages">

            {messages.map((message, index) => (

              <div
                key={index}
                className={`chat-message ${message.role}`}
              >

                <div className="chat-message-avatar">
                  {message.role === "user" ? "A" : "B"}
                </div>

                <div className="chat-message-content">

                  <p>
                    {message.content}
                  </p>

                  {message.evidence &&
                    message.evidence.length > 0 && (
                      <div className="chat-evidence">

                        <span className="evidence-label">
                          SOURCE EVIDENCE
                        </span>

                        {message.evidence.map(
                          (item, evidenceIndex) => (
                            <div
                              className="chat-evidence-item"
                              key={evidenceIndex}
                            >

                              <div className="evidence-meta">
                                <span>
                                  {item.source}
                                </span>

                                <span>
                                  Page {item.page}
                                </span>
                              </div>

                              <p>
                                "{item.relevant_text}"
                              </p>

                            </div>
                          )
                        )}

                      </div>
                    )}

                </div>

              </div>

            ))}

            {isLoading && (
              <div className="chat-message assistant">

                <div className="chat-message-avatar">
                  B
                </div>

                <div className="chat-message-content">
                  <span className="chat-thinking">
                    Analyzing the brief...
                  </span>
                </div>

              </div>
            )}

          </div>

        )}


        {error && (
          <div className="chat-error">
            {error}
          </div>
        )}


        <form
          className="chat-input-area"
          onSubmit={handleSubmit}
        >

          <input
            type="text"
            placeholder={
              document
                ? "Ask something about this brief..."
                : "Upload a brief before using Analyst Chat"
            }
            value={input}
            onChange={(event) =>
              setInput(event.target.value)
            }
            disabled={!document || isLoading}
          />

          <button
            type="submit"
            disabled={
              !input.trim() ||
              !document ||
              isLoading
            }
          >
            →
          </button>

        </form>

      </div>

    </section>
  );
}


export default AnalystChat;