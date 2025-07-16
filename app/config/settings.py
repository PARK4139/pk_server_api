from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "changeme"
    DB_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
