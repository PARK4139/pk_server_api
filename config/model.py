from dataclasses import dataclass
import toml


@dataclass
class UvicornConfig:
    protocol_type: str
    host: str
    port: int

    @property
    def url(self) -> str:
        return f"{self.protocol_type}://{self.host}:{self.port}"
 