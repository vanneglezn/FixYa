from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import admin_service
from app.schemas.admin_schema import AdminDashboardResponse
from app.dependencies import solo_admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin Dashboard"]
)


@router.get("/dashboard", response_model=AdminDashboardResponse)
def obtener_dashboard_admin(
    db: Session = Depends(get_db),
    current_user: dict = Depends(solo_admin)
):
    return admin_service.obtener_dashboard_admin(db)