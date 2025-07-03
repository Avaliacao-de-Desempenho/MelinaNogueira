import os
import io
from dotenv import load_dotenv
from google import generativeai as genai
from PIL import Image

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

def extract_data_from_invoice(file_bytes: bytes) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")

    image = Image.open(io.BytesIO(file_bytes))

    response = model.generate_content([PROMPT, image])

    return response.text
