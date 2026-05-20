# fastapi로 REST API 서버 구축

## 1. 가상환경 생성하고 활성화

venv 내부에 설치되고 프로젝트별로 환경을 분리할 수 있습니다.

```sh
cd D:\pythonwork\fastapi-oracle-api
python -m venv venv
venv\Scripts\activate
```

```sh
#비활성화
venv\Scripts\deactivate
```

## 2. 패키지 관리

#### 패키시 설치

```sh
pip install fastapi uvicorn sqlalchemy oracledb python-dotenv

#fastapi : 프레임워크
#uvicorn : ASGI 서버
#sqlalchemy(씨퀄 앨커미) : ORM
#oracledb : Oracle DB 드라이버
#python-dotenv : 환경변수 관리
#pydantic_settings : 파이썬 애플리케이션의 설정을 관리하고 검증
#Pydantic 파이썬 타입 어노테이션을 활용하여 데이터의 유효성을 검사
```

#### 패키지 관리

현재 가상환경에 설치된 python 패키지를 버전과 함께 작성하여 requirements.txt 파일에 저장

- requirements.txt 생성

```sh
pip freeze > requirements.txt
```

- requirements.txt 파일을 이용하여 패키지 설치

```sh
pip install -r requirements.txt
```

## 3. 프로젝트 파일 구성

```
fastapi-oracle-api/
│
├── .env                             # 환경 변수를 모아두는 설정 파일
│
├── app/
│   ├── __pycache__                  # 실행 속도를 높이기 위해 자동으로 생성하는 캐시(임시 파일)
│   ├── __init__.py__                # 해당 폴더를 `패키지`로 인식하게 만드는 파일로 import가 가능해짐
│   ├── main.py                      # FastAPI 진입점
│   │
│   ├── core/
│   │   └── config.py                # 환경 변수, 설정 파일
│   │
│   ├── database/
│   │   ├── database.py              # DB 연결, Session, Base 설정
│   │
│   ├── models/
│   │   ├── employee.py              # Employee 모델
│   │   └── book.py                  # Book 모델
│   │
│   ├── repositories/
│   │   ├── employee_repository.py   # DB 접근 코드
│   │   └── book_repository.py
│   │
│   ├── routers/
│   │   ├── employee_routers.py      # 라우터 (FastAPI endpoint)
│   │   └── book_routers.py
│   │
│   ├── services/
│   │   ├── employee_service.py      # 비즈니스 로직
│   │   └── book_service.py
│   │
│   └── tests/
│       ├── connectTest.py           # 테스트
│       └── init__.py
│
├── Wallet_shop/                     # 오라클 지갑 폴더
│
├── venv/                            # 가상환경
│
├── requirements.txt
└── README.md

```

## 4. fastapi 서버 구축

[fastapi공식문서](https://fastapi.tiangolo.com/ko/)

#### 서버 만들기

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

#### 실행하기

```sh
uvicorn app.main:app --reload
```

## 5. 오라클 연결

#### Oracle Instant Client 설치

Oracle DB 서버 전체를 설치할 필요 없이 Python, Java, Node.js 등에서 클라이언트 프로그램만으로 DB 접속 가능하게 해줍니다.
Python에서 oracledb(or cx_Oracle)로 연결할 때 필수 라이브러리입니다.

다운로드 : https://www.oracle.com/database/technologies/instant-client/ winx64-64-downloads.html

#### wallet 파일 압축풀기

#### 연결 테스트

```python
import oracledb
import os

# --- 1. Oracle Instant Client 경로 (Windows만 필요) ---
oracledb.init_oracle_client(lib_dir=r"C:\instantclient_23_9")

# --- 2. Wallet 경로 설정 ---
os.environ["TNS_ADMIN"] = r"C:\Wallet_shop"  # Wallet 압축을 푼 폴더 경로

# --- 3. DB 접속 정보 ---
dsn = "tnsname(서비스명)"     # tnsnames.ora 안의 서비스 이름 (예: db2025_high)
username = "접속사용자계정"
password = "Autonomous DB 비밀번호"

# --- 4. 연결 시도 ---
try:
    connection = oracledb.connect(
        user=username,
        password=password,
        dsn=dsn
    )

    print("✅ Oracle Cloud 연결 성공!")

    # 테스트 쿼리 실행
    cursor = connection.cursor()
    cursor.execute("SELECT sysdate FROM dual")
    result = cursor.fetchone()
    print("서버 시간:", result[0])

except Exception as e:
    print("❌ 연결 실패:", e)

finally:
    if 'connection' in locals():
        connection.close()

```

> 📣 서버가 백그라운드로 동작하고 중지가 안될 때 PowerShell 관리자모드에서 실행

```sh
# 프로세스 확인
Get-Process python
# 프로세스 중지
Stop-Process -Name python -Force
```

![alt text](./images/python01.png)

## 6. SQLAlchemy

- Python ORM(Object Relational Mapper) 라이브러리
- Python 객체 → DB 테이블, Python 코드로 SQL 작성 가능
- 여러 DB(MySQL, PostgreSQL, Oracle 등) 지원
- 즉, Python 클래스와 객체를 DB 테이블과 매핑해서 편리하게 다루도록 해주는 도구입니다.

기본 구조: 3 Layer (Presentation / Service / Repository)
|계층 |역할 |위치|
|:--|:--|:--|
|Presentation Layer |API 엔드포인트 (요청/응답 처리) |app/api/ |
|Service Layer |비즈니스 로직 |app/services/|
|Repository Layer |DB 접근, SQLAlchemy 쿼리 |app/repositories/|
|(추가) |모델 정의, DB 세팅 |app/models/, app/core/|

#### DB 연결

wallet 안의 tnsnames.ora 파일의 DIRECTORY 수정했음

```
WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="D:/pythonwork/fastapi-oracle-api/Wallet_shop")))
SSL_SERVER_DN_MATCH=yes
```

```python
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

```

DB 연결 URL 지정시 패스워드에 특수문자가 있으면 인코딩 해야함.

- 퍼센트 인코딩

  > @ → %40  
  > ! → %21  
  > / → %2F

- 함수 이용

```python
import urllib.parse
encoded_password = urllib.parse.quote_plus(self.ORACLE_PASSWORD)
```

## Repository, Service, Router 생성

#### Repository

```python

```

#### Service

```python

```

#### Router

```python

```

#### 테스트

```
http://127.0.0.1:8000/api/employees
```

## pydantic (파이댄틱)

- FastAPI에서 데이터 검증(validation)과 설정 관리(config) 를 담당하는 핵심 라이브러리
- pydantic의 핵심은 모델(Model) 입니다. class로 작성하지만, 자동으로 타입 검사와 변환을 합니다.

```

```

pydantic 기능

| 기능             | 설명                     | 예시                                          |
| :--------------- | :----------------------- | :-------------------------------------------- |
| 기본값(default)  | 값이 없을 때 기본 설정   | is_active: bool = True                        |
| 검증(Validation) | 잘못된 타입 입력 시 에러 | age: int에 문자열 넣으면 오류                 |
| 데이터 변환      | 자동 타입 변환           | "1" → 1                                       |
| 중첩 모델        | 객체 안에 객체 포함 가능 | address: AddressModel                         |
| alias (별칭)     | JSON 키 이름 바꾸기      | user_name: str = Field(..., alias="username") |
