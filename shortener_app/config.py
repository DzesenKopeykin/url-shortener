from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "LOCAL"
    base_url: str = "http://127.0.0.1:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file: str = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Load settings for {settings.env_name}")
    return settings
