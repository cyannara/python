from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.services.employee_service import fetch_all_employees

router = APIRouter(prefix="/employees", tags=["employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_employees(db: Session = Depends(get_db)):
    return fetch_all_employees(db)
