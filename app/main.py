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
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        raise HTTPException(status_code=422, detail="Resposta do Gemini não está em JSON válido.")

#12.345.678/0001-90
def cnpj_validate(cnpj: str) -> bool:
    model = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
    return bool(re.match(model, cnpj))

def date_validate(data_str: str) -> bool:
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def value_validate(valor: str) -> bool:
    model = r"^R\$ (\d{1,3}(\.\d{3})*|\d+),\d{2}$"
    return bool(re.match(model, valor))   
    
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado.")

    contents = await file.read()

    try:
        response_text = extract_data(contents, file.filename)
        data = extract_json(response_text)

        if not (cnpj_validate)(data["cnpj"]):
            raise HTTPException(status_code=400, detail="CNPJ inválido.")
        
        if not (date_validate)(data["data_emissao"]):
            raise HTTPException(status_code=400, detail= "Data de emissão inválida")
        
        if not (value_validate)(data["valor_total"]):
            raise HTTPException(status_code=400, detail="Valor total inválido")
        
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