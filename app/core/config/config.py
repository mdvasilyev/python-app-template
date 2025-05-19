from functools import lru_cache
from typing import Literal

import yaml
from pydantic import BaseModel, Field, ValidationError


class AppConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000
    name: str = "My FastAPI App"
    debug: bool = True


class DBConfig(BaseModel):
    host: str = "localhost"
    port: int = 5432
    name: str = "postgres"
    user: str = "postgres"
    password: str = "postgres"
    pool_size: int = 15


class AuthConfig(BaseModel):
    secret_key: str
    algorithm: Literal["HS256", "RS256"] = "HS256"
    access_token_expire_minutes: int = Field(30, gt=0)


class LoggingConfig(BaseModel):
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    log_file: str = "logs/app.log"
    rotation: str = "10 MB"
    retention: str = "10 days"
    compression: str = "zip"


class GlobalConfig(BaseModel):
    app: AppConfig
    db: DBConfig
    auth: AuthConfig
    logging: LoggingConfig

    @classmethod
    def load(cls, file_path: str = "./config.yaml") -> "GlobalConfig":
        try:
            with open(file_path, "r") as f:
                data = yaml.safe_load(f)
            return cls(**data)
        except FileNotFoundError:
            raise RuntimeError(f"Configuration file '{file_path}' not found.")
        except ValidationError as e:
            raise RuntimeError(f"Invalid configuration:\n{e}")


@lru_cache(maxsize=1)
def get_config() -> GlobalConfig:
    return GlobalConfig.load()
