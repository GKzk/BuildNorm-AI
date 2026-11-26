from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "BuildNorm AI"
    app_env: str = "local"
    app_debug: bool = True
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://buildnorm:change_me_local_only@localhost:5432/buildnorm"
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str | None = None
    llm_provider: str = "none"
    llm_api_key: str | None = None
    llm_model: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
