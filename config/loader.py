from config.model import UvicornConfig
import toml
from typing import Any


def load_uvicorn_config(config: dict[str, Any]) -> UvicornConfig:
    try:
        uvicorn_raw = config["pk_uvicorn"]
        return UvicornConfig(
            protocol_type=uvicorn_raw["protocol_type"],
            host=uvicorn_raw["host"],
            port=uvicorn_raw["port"],
        )
    except KeyError as e:
        raise ValueError(f"Uvicorn 설정 누락: {e}")