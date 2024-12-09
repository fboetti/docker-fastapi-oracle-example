# -- Pure Python Imports -- #
import os
import typing
from functools import (
    lru_cache,
)
# -- Backend Requirements Imports -- #
from pydantic import SecretStr
from pydantic_settings import (
    BaseSettings,
)
# -- Backend Package Imports -- #
from src.core import (
    environment_variables_path,
)


__all__ = [
    "BackendSettings",
    "get_settings",
]


# -- Private Methods -- #

def _populate_env(
        values: dict,
) -> None:
    for key, value in values.items():
        os.environ[key] = str(value)


def _env_init_from_file() -> None:
    variables_dict: typing.Dict[str, str] = {}
    with open(os.path.join(environment_variables_path, "backend.env")) as env_file:
        for line in env_file:
            key, value = line.strip().split("=")
            variables_dict[key.lower()] = value

    _populate_env(variables_dict)


# -- Exposed Classes and Methods -- #


class BackendSettings(BaseSettings):
    """
    Provides settings used for the entire backend application.
    The following properties default values will be overwritten if envs are set.
    """

    # Database Parameters
    database_container_host: str
    database_container_port: int
    oracle_database_name: str
    oracle_user: str
    oracle_password: SecretStr

    def get_database_connection_string(self) -> str:
        _oracle_password: str = self.oracle_password.get_secret_value()
        return f"oracle+cx_oracle://{self.oracle_user}:{_oracle_password}@{self.database_container_host}:{self.database_container_port}/{self.oracle_database_name}"


@lru_cache()
def get_settings() -> BackendSettings:
    _env_init_from_file()
    return BackendSettings()
