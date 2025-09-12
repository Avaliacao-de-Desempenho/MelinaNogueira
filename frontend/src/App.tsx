import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Selecione um arquivo primeiro!");
    
    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      const res = await axios.post("http://localhost:8000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setData(res.data);
    } catch (err) {
      console.error(err);
      alert("Erro ao enviar arquivo");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "#111",
      color: "white",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      padding: "20px"
    }}>
      <h1 style={{ marginBottom: "20px" }}>NFe Data Extractor</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
        style={{ marginBottom: "10px" }}
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        style={{
          padding: "10px 20px",
          background: "#2563eb",
          border: "none",
          borderRadius: "8px",
          cursor: "pointer",
          color: "white",
          fontWeight: "bold"
        }}
      >
        {loading ? "Processando..." : "Enviar"}
      </button>

      {data && (
        <div style={{
          marginTop: "20px",
          background: "#222",
          padding: "15px",
          borderRadius: "8px",
          maxWidth: "500px",
          width: "100%",
          textAlign: "left"
        }}>
          <h2>📄 Dados extraídos:</h2>
          <pre style={{ whiteSpace: "pre-wrap" }}>
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}

export default App;
