#interaccion con modelo de datos pydantic con modelo de mongo 
#vamos a mejorar la jerarquia para la bd con mas clases haciendolo un objeto mas complejo
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

#Clase para el plan del usuario anual o mensual o gratis
class Plan(BaseModel):
    nombre: str
    fecha_inicio: datetime
    fecha_fin: datetime 

#clase para el logueo del usuario el conteo es para que no pueda subir mas archivos dependiendo del plan
class Logueo(BaseModel):
    fecha: datetime
    conteo: int

#clase para el plan del usuario
class usuarios(BaseModel):
    usuario: str
    email: str
    pass_hash: str
    rol: str
    pago: bool = False
    activo: bool = True
    logueo:Optional[Logueo]
    plan: Optional[Plan]
    disabled: bool = False