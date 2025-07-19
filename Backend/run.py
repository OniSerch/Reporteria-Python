from fastapi import FastAPI
from Backend.Routes import usuarios

app = FastAPI()
# Incluimos las rutas de usuarios en la aplicación FastAPI
app.include_router(usuarios.usuarios)
