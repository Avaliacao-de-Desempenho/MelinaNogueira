from fastapi import FastAPI, UploadFile, File, HTTPException
from app.gemini import extract_data
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

def extract_json(text: str) -> dict:
    cleaned = re.sub(r"^```(?:json)?\n?", "", text.strip())
    cleaned = re.sub(r"\n?```$", "", cleaned.strip())
    return json.loads(cleaned)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado.")

    contents = await file.read()

    try:
        response_text = extract_data(contents, file.filename)
        data = extract_json(response_text)

        await database.execute(
            notas_fiscais.insert().values(
                cnpj=data["cnpj"],
                data_emissao=datetime.strptime(data["data_emissao"], "%d/%m/%Y").date(),
                valor_total=data["valor_total"],
                data_registro=datetime.now()
            )
        )

        return {"extraido": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar com Gemini: {str(e)}")

@app.get("/notas")
async def notes():
    query = notas_fiscais.select()
    results = await database.fetch_all(query)
    
    notas_formatadas = []
    for nota in results:
        nota_dict = dict(nota)
        nota_dict["data_registro"] = nota_dict["data_registro"].strftime("%d/%m/%Y %H:%M")
        nota_dict["data_emissao"] = nota_dict["data_emissao"].strftime("%d/%m/%Y")
        notas_formatadas.append(nota_dict)

    return notas_formatadas
