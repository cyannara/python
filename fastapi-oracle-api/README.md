# FastAPI Oracle API

이 프로젝트는 FastAPI를 사용하여 Oracle 데이터베이스와 연동되는 REST API 서버를 구축하는 것을 목표로 합니다.

## 설치

1. 이 저장소를 클론합니다.
   ```bash
   git clone <repository-url>
   cd fastapi-oracle-api
   ```

2. 필요한 패키지를 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```

3. 환경 변수를 설정합니다. `.env` 파일을 수정하여 데이터베이스 연결 정보를 입력합니다.

## 실행

다음 명령어로 FastAPI 서버를 실행합니다.

```bash
uvicorn src.main:app --reload
```

## 테스트

테스트는 `tests/test_api.py` 파일에 정의되어 있습니다. 다음 명령어로 테스트를 실행할 수 있습니다.

```bash
pytest
```

## 기여

기여를 원하신다면, 이 저장소를 포크한 후 변경 사항을 제안해 주세요.