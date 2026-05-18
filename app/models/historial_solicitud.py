from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class HistorialSolicitud(Base):
    __tablename__ = "historial_solicitud"

    fecha_historial = Column(DateTime, primary_key=True, server_default=func.now())
    motivo = Column(String(300), nullable=False)
    estado = Column(String(30), nullable=False)
    solicitud_id_solicitud = Column(
        ForeignKey("solicitud.id_solicitud"),
        primary_key=True
    )
    usuario_rut = Column(String(12), ForeignKey("usuario.rut"), nullable=False)
    