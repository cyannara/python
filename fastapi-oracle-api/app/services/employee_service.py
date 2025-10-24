from app.repositories.employee_repository import get_all_employees
from sqlalchemy.orm import Session

def fetch_all_employees(db: Session):
    employees = get_all_employees(db)
    return employees
