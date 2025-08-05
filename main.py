

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Recipe API with OAuth2")

# Permitir solicitudes desde cualquier origen (para desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz de prueba
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Recetas con OAuth2"}
