from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.services import solicitud_service

from app.schemas.solicitud_schema import (
    SolicitudCreate,
    SolicitudUpdate,
    SolicitudResponse,
    SolicitudEstadoUpdate
)

router = APIRouter(
    prefix="/solicitudes",
    tags=["Solicitudes"]
)

# CREAR SOLICITUD
@router.post("/", response_model=SolicitudResponse)
def crear_solicitud(
    solicitud: SolicitudCreate,
    db: Session = Depends(get_db)
):
    return solicitud_service.crear_solicitud(db, solicitud)


# LISTAR SOLICITUDES
@router.get("/", response_model=List[SolicitudResponse])
def listar_solicitudes(db: Session = Depends(get_db)):
    return solicitud_service.listar_solicitudes(db)


# CAMBIAR ESTADO SOLICITUD
@router.put("/{id_solicitud}/estado", response_model=SolicitudResponse)
def cambiar_estado_solicitud(
    id_solicitud: int,
    data: SolicitudEstadoUpdate,
    db: Session = Depends(get_db)
):
    solicitud = solicitud_service.cambiar_estado_solicitud(
        db,
        id_solicitud,
        data
    )

    if solicitud is None:
        raise HTTPException(
            status_code=404,
            detail="Solicitud no encontrada"
        )

    if solicitud == "ESTADO_INVALIDO":
        raise HTTPException(
            status_code=400,
            detail="Estado de trabajo inválido"
        )

    return solicitud


# OBTENER SOLICITUD POR ID
@router.get("/{id_solicitud}", response_model=SolicitudResponse)
def obtener_solicitud(
    id_solicitud: int,
    db: Session = Depends(get_db)
):
    solicitud = solicitud_service.obtener_solicitud(
        db,
        id_solicitud
    )

    if not solicitud:
        raise HTTPException(
            status_code=404,
            detail="Solicitud no encontrada"
        )

    return solicitud


# ACTUALIZAR SOLICITUD
@router.put("/{id_solicitud}", response_model=SolicitudResponse)
def actualizar_solicitud(
    id_solicitud: int,
    solicitud: SolicitudUpdate,
    db: Session = Depends(get_db)
):
    solicitud_actualizada = solicitud_service.actualizar_solicitud(
        db,
        id_solicitud,
        solicitud
    )

    if not solicitud_actualizada:
        raise HTTPException(
            status_code=404,
            detail="Solicitud no encontrada"
        )

    return solicitud_actualizada


# ELIMINAR SOLICITUD
@router.delete("/{id_solicitud}")
def eliminar_solicitud(
    id_solicitud: int,
    db: Session = Depends(get_db)
):
    solicitud_eliminada = solicitud_service.eliminar_solicitud(
        db,
        id_solicitud
    )

    if not solicitud_eliminada:
        raise HTTPException(
            status_code=404,
            detail="Solicitud no encontrada"
        )

    return {
        "mensaje": "Solicitud desactivada correctamente"
    }