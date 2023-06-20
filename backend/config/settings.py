from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    APP_NAME: str = Field(env="APP_NAME", default="TODO List")
    DEBUG: bool = Field(env="DEBUG", default=True)

    # DATABASE_URL: str = Field(env="DATABASE_URL")

    # API Docs
    API_DOCS_URL: str | None = Field(env="API_DOCS_URL", default=None)
    API_REDOC_URL: str | None = Field(env="API_REDOC_URL", default=None)
    API_OPENAPI_URL: str | None = Field(env="API_OPENAPI_URL", default=None)

    class Config:
        env_file_encoding = "utf-8"
