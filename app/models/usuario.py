from sqlalchemy import Column, String, Date, Boolean, ForeignKey, Integer, DateTime
from app.database import Base
from datetime import datetime
from sqlalchemy import Enum as SqlEnum
from app.enums.usuario_enum import TipoUsuario


class Usuario(Base):

    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)

    rut = Column(String, unique=True, nullable=False)
    nombre_completo = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(String, nullable=False)

    correo = Column(String, unique=True, nullable=False)
    telefono = Column(String)

    contrasena = Column(String, nullable=False)

    estado_usuario = Column(Boolean, default=True)

    comuna_id_comuna = Column(
        ForeignKey("comuna.id_comuna"),
        nullable=False
    )

    tipo_usuario = Column(SqlEnum(TipoUsuario), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)