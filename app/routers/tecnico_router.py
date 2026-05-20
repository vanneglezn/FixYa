from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func
from app.models.resena import Resena
from app.models.solicitud import Solicitud
from sqlalchemy import desc


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
@router.get("/{rut}/rating")
def obtener_rating_tecnico(
    rut: str,
    db: Session = Depends(get_db)
):
    promedio = db.query(
        func.avg(Resena.calificacion)
    ).join(
        Solicitud,
        Solicitud.id_solicitud == Resena.solicitud_id_solicitud
    ).filter(
        Solicitud.tecnico_usuario_rut == rut,
        Resena.resena_activa == "S"
    ).scalar()

    total = db.query(Resena).join(
        Solicitud,
        Solicitud.id_solicitud == Resena.solicitud_id_solicitud
    ).filter(
        Solicitud.tecnico_usuario_rut == rut,
        Resena.resena_activa == "S"
    ).count()

    return {
        "tecnico_usuario_rut": rut,
        "promedio_calificacion": round(float(promedio), 1) if promedio else 0,
        "total_resenas": total
    }
    
@router.get("/top-rating")
def obtener_top_tecnicos(
    db: Session = Depends(get_db)
):
    resultados = db.query(
        Solicitud.tecnico_usuario_rut,
        func.avg(Resena.calificacion).label("promedio"),
        func.count(Resena.id_resena).label("total_resenas")
    ).join(
        Solicitud,
        Solicitud.id_solicitud == Resena.solicitud_id_solicitud
    ).filter(
        Resena.resena_activa == "S"
    ).group_by(
        Solicitud.tecnico_usuario_rut
    ).order_by(
        desc("promedio")
    ).limit(10).all()

    return [
        {
            "tecnico_usuario_rut": r.tecnico_usuario_rut,
            "promedio_calificacion": round(float(r.promedio), 1),
            "total_resenas": r.total_resenas
        }
        for r in resultados
    ]