import os
from dotenv import load_dotenv
from google import generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT = """From this receipt image, extract the following fields:
- CNPJ (Brazilian company registry number)
- Issue Date (Data de Emissão)
- Total Amount (Valor Total)

Ignore any extra text. Return exactly and only the fields requested and pay attention to variations such as "Valor Total", "TOTAL", or "Total a pagar".

Return only these 3 fields in JSON format, like this:

{
  "cnpj": "00.000.000/0000-00",
  "data_emissao": "DD/MM/YYYY",
  "valor_total": "R$ 0,00"
}
"""

def extract_data_from_invoice(file_bytes: bytes, filename: str) -> str:
    temp_path = f"/tmp/{filename}" if os.name != "nt" else f"{filename}"

    with open(temp_path, "wb") as f:
        f.write(file_bytes)

    uploaded_file = genai.upload_file(temp_path)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([uploaded_file, PROMPT])

    os.remove(temp_path)
    return response.text
