import oracledb
import os

# --- 1. Oracle Instant Client 경로 (Windows만 필요) ---
oracledb.init_oracle_client(lib_dir=r"D:/pythonwork/fastapi-oracle-api/instantclient_23_9")

# --- 2. Wallet 압축을 푼 폴더 경로 설정 TNS_ADMIN 환경변수는 고정임 ---
os.environ["TNS_ADMIN"] = r"D:/pythonwork/fastapi-oracle-api/Wallet_shop"

# --- 3. DB 접속 정보 ---

dsn = "shop_high"           # tnsnames.ora 안의 서비스 이름 (예: db2025_high)
username = "shopuser"       # 사용자 계정
password = "Shop4212460!@"  # Autonomous DB 비밀번호

# --- 4. 연결 시도 ---
try:
    connection = oracledb.connect(
        user=username,
        password=password,
        dsn=dsn
    )

    print("✅ Oracle Cloud 연결 성공!", connection.version)

    # 테스트 쿼리 실행
    cursor = connection.cursor()
    #cursor.execute("SELECT sysdate FROM dual")
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchone()
    print("서버 시간:", result)

except Exception as e:
    print("❌ 연결 실패:", e)

finally:
    if 'connection' in locals():
        connection.close()
