from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int

    RATE_LIMIT_PER_MINUTE: int

    FAISS_INDEX_PATH: str
    DOCUMENT_STORAGE_PATH: str

    class Config:
        env_file = ".env"


settings = Settings()