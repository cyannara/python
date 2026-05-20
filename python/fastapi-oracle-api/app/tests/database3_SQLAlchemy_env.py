import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import oracledb
from dotenv import load_dotenv
import urllib.parse

# SQLAlchemy를 이용하여 환경변수 이용하여 Oracle DB에 연결

load_dotenv()

# --- 1. Oracle Instant Client 초기화 ---
oracledb.init_oracle_client(lib_dir=os.getenv("INSTANT_CLIENT_DIR"))

# --- 2. Wallet 경로 환경 변수 ---
os.environ["TNS_ADMIN"] = os.getenv("ORACLE_WALLET_PATH")

# --- 3. 접속정보 ---
user = os.getenv("ORACLE_USER")
password = urllib.parse.quote_plus(os.getenv("ORACLE_PASSWORD"))
dsn = os.getenv("ORACLE_DSN")

DATABASE_URL = f"oracle+oracledb://{user}:{password}@{dsn}"

# --- 4. SQLAlchemy 연결 ---
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

session = SessionLocal()

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    emp_no = Column(Integer, primary_key=True, autoincrement=True)
    emp_name = Column(String(100))
    # Book과 1:N 관계 (optional, Book 모델 필요)
    # books = relationship("Book", back_populates="employee")    

# 데이터 추가
new_emp = Employee(emp_name="yumi", emp_no=1234)
session.add(new_emp)
session.commit()  # DB에 실제 반영

# 데이터 조회
employees = session.query(Employee).all()
for emp in employees:
    print(emp.emp_no, emp.emp_name)