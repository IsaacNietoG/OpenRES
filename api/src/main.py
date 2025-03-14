from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

app = FastAPI(
    title="OpenRES API",
    description="API para el almacenamiento seguro de variables de entorno",
    version="0.1.0"
)

class Secret(BaseModel):
    key: str
    value: str
    environment: str
    project: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Bienvenido a OpenRES API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/secrets/", status_code=status.HTTP_201_CREATED)
async def create_secret(secret: Secret):
    # TODO: Implementar la lógica de cifrado usando el módulo de Go
    return {"message": "Secreto creado exitosamente"}

@app.get("/secrets/{project}")
async def get_secrets(project: str, environment: str):
    # TODO: Implementar la lógica de descifrado usando el módulo de Go
    return {"message": f"Secretos del proyecto {project} en ambiente {environment}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 