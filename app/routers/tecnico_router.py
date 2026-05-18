from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.tecnico_schema import TecnicoCreate, TecnicoUpdate, TecnicoResponse
from app.services import tecnico_service

router = APIRouter(
    prefix="/tecnicos",
    tags=["Técnicos"]
)

@router.post("/", response_model=TecnicoResponse)
def crear_tecnico(tecnico: TecnicoCreate, db: Session = Depends(get_db)):
    nuevo_tecnico = tecnico_service.crear_tecnico(db, tecnico)

    if not nuevo_tecnico:
        raise HTTPException(status_code=400, detail="El técnico ya existe")

    return nuevo_tecnico


@router.get("/", response_model=List[TecnicoResponse])
def listar_tecnicos(db: Session = Depends(get_db)):
    return tecnico_service.listar_tecnicos(db)


@router.get("/{rut}", response_model=TecnicoResponse)
def obtener_tecnico(rut: str, db: Session = Depends(get_db)):
    tecnico = tecnico_service.obtener_tecnico(db, rut)

    if not tecnico:
        raise HTTPException(status_code=404, detail="Técnico no encontrado")

    return tecnico


@router.put("/{rut}", response_model=TecnicoResponse)
def actualizar_tecnico(rut: str, tecnico: TecnicoUpdate, db: Session = Depends(get_db)):
    tecnico_actualizado = tecnico_service.actualizar_tecnico(db, rut, tecnico)

    if not tecnico_actualizado:
        raise HTTPException(status_code=404, detail="Técnico no encontrado")

    return tecnico_actualizado


@router.delete("/{rut}")
def eliminar_tecnico(rut: str, db: Session = Depends(get_db)):
    tecnico_eliminado = tecnico_service.eliminar_tecnico(db, rut)

    if not tecnico_eliminado:
        raise HTTPException(status_code=404, detail="Técnico no encontrado")

    return {"mensaje": "Técnico eliminado correctamente"}