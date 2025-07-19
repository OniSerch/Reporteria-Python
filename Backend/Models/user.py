#interaccion con modelo de datos pydantic con modelo de mongo 
from typing import Optional
from pydantic import BaseModel

class usuarios(BaseModel):
    id: Optional[str]
    username: str
    email: str
    full_name: str
    disabled: bool = False