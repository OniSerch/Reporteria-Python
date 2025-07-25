from fastapi import FastAPI
from Backend.Routes import usuarios
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Usuarios",
    description="API para gestionar usuarios",
)
# Incluimos las rutas de usuarios en la aplicación FastAPI
app.include_router(usuarios.usuarios)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue corre en el puerto 5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
