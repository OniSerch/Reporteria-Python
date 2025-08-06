#importamos las rutas y para subir archivos 
from fastapi import APIRouter,UploadFile,File
from Backend.utils.rust_bridge import analizar_archivo
import tempfile
router = APIRouter()
@router.post("/analizar")
async def analizar(file:UploadFile=File(...)):
    with tempfile.NamedTemporaryFile(delete=False,suffix=".csv")as tmp:
        tmp.write(await file.read())
        tmp_path=tmp.name
    resultado=analizar_archivo(tmp_path)
    return resultado