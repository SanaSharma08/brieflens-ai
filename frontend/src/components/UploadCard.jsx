import { useRef, useState } from "react";

function UploadCard({ onAnalysisComplete }) {
  const fileInputRef = useRef(null);

  const [selectedFile, setSelectedFile] = useState(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [error, setError] = useState("");

  const handleFileSelect = (event) => {
    const file = event.target.files[0];

    if (!file) {
      return;
    }

    if (file.type !== "application/pdf") {
      setError("Please select a PDF file.");
      event.target.value = "";
      return;
    }

    if (file.size > 10 * 1024 * 1024) {
      setError("The PDF must be smaller than 10 MB.");
      event.target.value = "";
      return;
    }

    setError("");
    setSelectedFile(file);
  };

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleAnalyze = async () => {
    if (!selectedFile) {
      return;
    }

    setIsAnalyzing(true);
    setError("");

    try {
      const formData = new FormData();

      formData.append("file", selectedFile);

      const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/api/analyze`, {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        const errorData = await response.json();

        throw new Error(
          errorData.detail || "Analysis failed."
        );
      }

      const analysis = await response.json();

      onAnalysisComplete({
        analysis,
        fileName: selectedFile.name,
        });
    } catch (error) {
      console.error("Analysis error:", error);
      setError(
        error.message ||
        "Something went wrong while analyzing the document."
      );
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="upload-card">
      <input
        ref={fileInputRef}
        type="file"
        accept=".pdf,application/pdf"
        onChange={handleFileSelect}
        hidden
      />

      {!selectedFile ? (
        <>
          <div className="upload-icon">↑</div>

          <h3>Analyze a client brief</h3>

          <p>
            Upload a PDF to generate your first structured analysis.
          </p>

          <button
            className="upload-button"
            onClick={handleUploadClick}
          >
            Upload PDF
          </button>

          <span className="upload-hint">
            PDF files only · Max 10 MB
          </span>
        </>
      ) : (
        <>
          <div className="upload-icon">
            {isAnalyzing ? "..." : "✓"}
          </div>

          <h3>{selectedFile.name}</h3>

          <p>
            {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
          </p>

          {error && (
            <p className="upload-error">
              {error}
            </p>
          )}

          <button
            className="upload-button"
            onClick={handleAnalyze}
            disabled={isAnalyzing}
          >
            {isAnalyzing
              ? "Analyzing..."
              : "Analyze Brief"}
          </button>

          {!isAnalyzing && (
            <button
              className="change-file-button"
              onClick={handleUploadClick}
            >
              Choose another file
            </button>
          )}
        </>
      )}
    </div>
  );
}

export default UploadCard;