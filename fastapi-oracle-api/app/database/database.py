from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
import urllib.parse
import oracledb

# thick 모드 초기화
oracledb.init_oracle_client(
    lib_dir=settings.INSTANT_CLIENT_DIR, 
    config_dir=settings.ORACLE_WALLET_PATH
)


Base = declarative_base()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
