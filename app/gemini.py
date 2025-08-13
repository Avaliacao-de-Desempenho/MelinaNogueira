import os
from dotenv import load_dotenv
from google import generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT = """From this receipt image, extract the following fields:
- CNPJ (Brazilian company registry number) - return in format 00.000.000/0000-00
- Issue Date (Data de Emissão) - must be formatted as DD/MM/YYYY (convert from other date formats if needed)
- Total Amount (Valor Total) - must include "R$" and use comma as decimal separator

Important requirements:
1. Return ONLY plain JSON output without any markdown, backticks, or additional text
2. Format dates exactly as DD/MM/YYYY (convert from DD.MM.YYYY or other formats if present)
3. Total amount must be formatted as "R$ X,XX" 
4. CNPJ must be properly formatted with punctuation
5. Do not include any other fields or explanations

Example of required output format:
{
  "cnpj": "00.000.000/0000-00",
  "data_emissao": "DD/MM/YYYY",
  "valor_total": "R$ 0,00"
}

Do not deviate from this format. Do not add any text outside the JSON structure. If a field is missing or unclear, return null for that field but maintain the JSON structure.
"""

def extract_data(file_bytes: bytes, filename: str) -> str:
    temp_path = f"/tmp/{filename}" if os.name != "nt" else f"{filename}"

    with open(temp_path, "wb") as f:
        f.write(file_bytes)

    uploaded_file = genai.upload_file(temp_path)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        [uploaded_file, PROMPT],
        generation_config={"response_mime_type": "application/json"}
    )

    os.remove(temp_path)
    return response.text