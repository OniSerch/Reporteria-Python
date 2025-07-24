from fastapi import FastAPI
from Backend.Routes import usuarios

app = FastAPI(
    title="API de Usuarios",
    description="API para gestionar usuarios",
)
# Incluimos las rutas de usuarios en la aplicación FastAPI
app.include_router(usuarios.usuarios)
