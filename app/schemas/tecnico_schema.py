from pydantic import BaseModel, Field
from typing import Optional, List

class TecnicoCreate(BaseModel):
    usuario_rut: str
    descripcion_perfil: str
    experiencia_anios: int = Field(ge=0)
    nivel_tecnico: str
    servicios: List[int]
    comunas: List[int]

class TecnicoUpdate(BaseModel):
    descripcion_perfil: Optional[str] = None
    experiencia_anios: Optional[int] = Field(default=None, ge=0)
    nivel_tecnico: Optional[str] = None
    tecnico_verificado: Optional[bool] = None

class TecnicoResponse(BaseModel):
    usuario_rut: str
    descripcion_perfil: str
    experiencia_anios: int
    nivel_tecnico: str
    tecnico_verificado: bool

    class Config:
        from_attributes = True