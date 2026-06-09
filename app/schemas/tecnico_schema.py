from pydantic import BaseModel, Field
from typing import Optional, List, Literal

class TecnicoCreate(BaseModel):
    usuario_rut: str
    descripcion_perfil: str
    experiencia_anios: int = Field(ge=0)
    nivel_tecnico: Literal['Basico','Intermedio','Avanzado']
    servicios: List[int]
    comunas: List[int]

class TecnicoUpdate(BaseModel):
    descripcion_perfil: Optional[str] = None
    experiencia_anios: Optional[int] = Field(default=None, ge=0)
    nivel_tecnico: Optional[Literal['Basico','Intermedio','Avanzado']] = None
    tecnico_verificado: Optional[bool] = None

class TecnicoResponse(BaseModel):
    usuario_rut: str
    descripcion_perfil: str
    experiencia_anios: int
    nivel_tecnico: str
    tecnico_verificado: bool

    class Config:
        from_attributes = True