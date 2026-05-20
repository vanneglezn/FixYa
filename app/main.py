from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles

from app.database import engine, Base

from app.models import usuario, comuna, region
from app.models import tecnico, tecnico_servicio, tecnico_comuna
from app.models import solicitud, servicio, cotizacion
from app.models import historial_solicitud, resena

from app.routers.usuario_router import router as usuario_router
from app.routers.tecnico_router import router as tecnico_router
from app.routers.solicitud_router import router as solicitud_router
from app.routers.cotizacion_router import router as cotizacion_router
from app.routers.historial_solicitud_router import router as historial_solicitud_router
from app.routers import resena_router
from app.routers import documento_tecnico_router
from app.routers import admin_router
from app.routers import region_router
from app.routers import comuna_router
from app.routers import servicio_router
from app.routers import tecnico_servicio_router
from app.routers import tecnico_comuna_router


app = FastAPI(
    title="FixYa API",
    version="1.0.0"
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="FixYa API",
        version="1.0.0",
        description="API FixYa",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


Base.metadata.create_all(bind=engine)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(usuario_router)
app.include_router(tecnico_router)
app.include_router(solicitud_router)
app.include_router(cotizacion_router)
app.include_router(historial_solicitud_router)
app.include_router(resena_router.router)
app.include_router(documento_tecnico_router.router)
app.include_router(admin_router.router)
app.include_router(region_router.router)
app.include_router(comuna_router.router)
app.include_router(servicio_router.router)
app.include_router(tecnico_servicio_router.router)
app.include_router(tecnico_comuna_router.router)

@app.get("/")
def root():
    return {
        "mensaje": "FixYa funcionando"
    }