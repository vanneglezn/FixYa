from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

# ---------------------------------------------------
# DB SESSION
# ---------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------
# AUTH PLACEHOLDER (por ahora simple)
# ---------------------------------------------------
def get_current_user():
    return {
        "mensaje": "usuario autenticado (placeholder)"
    }