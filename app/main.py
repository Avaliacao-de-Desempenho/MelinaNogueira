from fastapi import FastAPI, UploadFile, File, HTTPException
from app.gemini import extract_data_from_invoice
from app.db import database, notas_fiscais
from datetime import datetime
import json

app = FastAPI()
ALLOWED_TYPES = ["image/jpeg", "image/png"]

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado.")
    
    contents = await file.read()
    
    try:
        result_text = extract_data_from_invoice(contents)

        data = json.loads(result_text)

        data_emissao = datetime.strptime(data["data_emissao"], "%d/%m/%Y").date()

        query = notas_fiscais.insert().values(
            cnpj=data["cnpj"],
            data_emissao=data_emissao,
            valor_total=data["valor_total"]
        )

        await database.execute(query)

        return {"extraido": data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao usar Gemini: {str(e)}")
