from fastapi import FastAPI, UploadFile, File, HTTPException
from app.gemini import extract_data_from_invoice
from app.db import database, notas_fiscais
from datetime import datetime
import json
import re

app = FastAPI()

ALLOWED_TYPES = ["image/jpeg", "image/png", "application/pdf"]

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "API de extração de NFe funcionando"}

def extract_json_from_response(text: str) -> dict:
    cleaned = re.sub(r"^```(?:json)?\n?", "", text.strip())
    cleaned = re.sub(r"\n?```$", "", cleaned.strip())
    return json.loads(cleaned)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado.")

    contents = await file.read()

    try:
        response_text = extract_data_from_invoice(contents, file.filename)
        print(response_text)
        
        data = extract_json_from_response(response_text)

        await database.execute(
            notas_fiscais.insert().values(
                cnpj=data["cnpj"],
                data_emissao=datetime.strptime(data["data_emissao"], "%d/%m/%Y").date(),
                valor_total=data["valor_total"]
            )
        )

        return {"extraido": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar com Gemini: {str(e)}")

@app.get("/notas")
async def listar_notas():
    query = notas_fiscais.select()
    results = await database.fetch_all(query)
    return results

