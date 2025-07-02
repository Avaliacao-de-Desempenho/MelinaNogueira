# API

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse #Para retornar em JSON

app = FastAPI()

ALLOWED_TYPES = ["image/jpeg", "image/png", "application/pdf"]

@app.get("/")
def read_root():
    return {"message": "API de extração de NFe funcionando 🎉"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=415, detail="Tipo de arquivo não suportado.")

    contents = await file.read()
    file_size_kb = round(len(contents) / 1024, 2)

    return JSONResponse(
        content={
            "filename": file.filename,
            "size_kb": file_size_kb,
            "type": file.content_type
        }
    )