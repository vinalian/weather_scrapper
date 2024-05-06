from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Настройки для подключения к базе данных PostgreSQL
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    SCRAPPER_INTERVAL: int
    SCRAPPER_LATITUDE: float
    SCRAPPER_LONGITUDE: float

    class Config:
        env_file = ".env"


settings = Settings()
