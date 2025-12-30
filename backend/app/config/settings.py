# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Grievance AI System"
    ENVIRONMENT: str = "demo"
    LOG_LEVEL: str = "INFO"

settings = Settings()
