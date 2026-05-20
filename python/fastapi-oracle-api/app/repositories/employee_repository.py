from app.models.employee import Employee
from sqlalchemy.orm import Session

def get_all_employees(db: Session):
    return db.query(Employee).all()
