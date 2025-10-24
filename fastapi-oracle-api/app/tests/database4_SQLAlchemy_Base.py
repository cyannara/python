from app.database.database import SessionLocal
from app.models.employee import Employee

# SQLAlchemy 모듈화(Database, Models) 후 테스트 코드

# 세션 생성
session = SessionLocal()

# 조회 예제
employees = session.query(Employee).all()
for emp in employees:
    print(emp.emp_no, emp.emp_name)
  #  for book in emp.books:
  #      print(" -", book.title)

session.close()
