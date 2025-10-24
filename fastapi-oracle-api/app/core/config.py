from pydantic_settings import BaseSettings
import urllib.parse

# pydantic은 설정 파일(.env)을 읽어서 객체로 관리

class Settings(BaseSettings):
    ORACLE_USER: str
    ORACLE_PASSWORD: str
    ORACLE_DSN: str
    ORACLE_WALLET_PATH: str
    INSTANT_CLIENT_DIR: str

    @property
    def DATABASE_URL(self):
        #비밀번호 인코딩
        encoded_password = urllib.parse.quote_plus(self.ORACLE_PASSWORD)
        return (
            f"oracle+oracledb://{self.ORACLE_USER}:{encoded_password}"
            f"@{self.ORACLE_DSN}"
        )

    class Config:
        env_file = ".env"

settings = Settings()
