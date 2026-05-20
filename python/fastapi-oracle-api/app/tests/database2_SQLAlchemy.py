from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import oracledb

# SQLAlchemy를 이용하여 Oracle DB에 연결하고,
# 데이터를 추가 및 조회하는 예제입니다.

# Oracle Instant Client 초기화
oracledb.init_oracle_client(
    lib_dir="D:/pythonwork/fastapi-oracle-api/instantclient_23_9",
    config_dir="D:/pythonwork/fastapi-oracle-api/Wallet_shop"
)

# DB 연결                                              '%40'는 '@'의 인코딩 값
DATABASE_URL = f"oracle+oracledb://shopuser:Shop4212460!%40@shop_high"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    emp_no = Column(Integer, primary_key=True, autoincrement=True)
    emp_name = Column(String(100))


# 데이터 조회
employees = session.query(Employee).all()
for emp in employees:
    print(emp.emp_no, emp.emp_name)

session.close()
