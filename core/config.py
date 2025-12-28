"""Pydantic Settings (чтение .env)"""
from pydantic import PostgresDsn, RedisDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Any, Optional


class Settings(BaseSettings):
    """Класс настроек"""
    
    # Подгружаем файл .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True  # Переменные в .env будут в верхнем регистре
    )
    # FastAPI
    PROJECT_NAME: str
    VERSION: str
    API_V1_STR: str

    # Postgres
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str = 5432
    POSTGRES_DB: str
    

    # Сборка URL для SQLAlchemy (asyncpg)
    DATABASE_URL = Optional[str] = None

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], values: Any) -> Any:
        """Функция сборки URL для SQLAlchemy"""

        # Если DATABASE_URL не None, то возвращаем его
        if isinstance(v, str):
            return v
        else:
            data = values.data
            return (
                f"postgresql+asyncpg://{data.POSTGRES_USER}:{data.POSTGRES_PASSWORD}@"
                    f"{data.POSTGRES_HOST}:{data.POSTGRES_PORT}/{data.POSTGRES_DB}"
            )
    # redis
    REDIS_HOST: str
    REDIS_PORT: str = 6379

    @property
    def CELERY_BROKER_URL(self) -> dict:
        """Функция сборки URL для Celery"""
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


# Экземляр настроек для других модулей
settings = Settings()
