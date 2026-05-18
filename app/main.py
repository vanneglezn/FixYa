from fastapi import FastAPI

from app.database import engine, Base

from app.models import usuario, comuna, region
from app.models import tecnico, tecnico_servicio, tecnico_comuna
from app.models import solicitud
from app.models import servicio
from app.models import cotizacion

from app.routers.usuario_router import router as usuario_router
from app.routers.tecnico_router import router as tecnico_router
from app.routers.solicitud_router import router as solicitud_router
from app.routers.cotizacion_router import router as cotizacion_router

app = FastAPI(
    title="FixYa API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(usuario_router)
app.include_router(tecnico_router)
app.include_router(solicitud_router)
app.include_router(cotizacion_router)

@app.get("/")
def root():

    return {
        "mensaje": "FixYa funcionando"
    }