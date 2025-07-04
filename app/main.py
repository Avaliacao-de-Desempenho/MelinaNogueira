from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.gemini import extract_data_from_invoice

app = FastAPI()

ALLOWED_TYPES = ["image/jpeg", "image/png", "application/pdf"]

@app.get("/")
def read_root():
    return {"message": "API de extração de NFe funcionando"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado.")

    contents = await file.read()

    try:
        result = extract_data_from_invoice(contents, file.filename)
        return {"extraido": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar com Gemini: {str(e)}")
