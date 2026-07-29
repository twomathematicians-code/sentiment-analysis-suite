from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    model_cache_dir: str = "/app/.model_cache"
    batch_max_size: int = 100
    default_language: str = "en"

@lru_cache
def get_settings() -> Settings:
    return Settings()
