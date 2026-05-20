from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Employee(Base):
    __tablename__ = "employees"

    emp_no = Column(Integer, primary_key=True, autoincrement=True)
    emp_name = Column(String(100))
    # Book과 1:N 관계 (optional, Book 모델 필요)
    # books = relationship("Book", back_populates="employee")    