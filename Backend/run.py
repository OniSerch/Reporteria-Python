from fastapi import FastAPI

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una ruta básica
@app.get("/")
def read_root():
    return {"message": "Hello World"}