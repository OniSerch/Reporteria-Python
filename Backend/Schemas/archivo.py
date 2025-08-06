from pydantic import BaseModel
class ResultadoAnalisis(BaseModel):
    rows:int
    colums:int
    columnas:list[str]
    vacios_por_columna:dict
    resumen_numerico:dict
    