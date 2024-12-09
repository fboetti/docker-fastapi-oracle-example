# -- Pure Python Imports -- #
import enum
import typing
# -- Backend Requirements Imports -- #
from sqlalchemy import (
    Column,
    Enum as SqlAlchemyEnum,
    Integer,
    String,
)
# -- Backend Package Imports -- #
from src.api.models.base import (
    SqlAlchemyBase,
    PydanticBaseModel,
)

__all__ = [
    "User",
    "UserGender",
    "UserPydanticSchema",
    "UserCreatePydanticSchema",
]


# -- ORM Models -- #

class UserGender(enum.Enum):
    male: str = "male"
    female: str = "female"
    other: str = "other"


class User(SqlAlchemyBase):
    """
    Users of the application.
    """

    __tablename__ = "test_users"

    id: Column = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )
    first_name: Column = Column(
        String(50),
        nullable=True,
    )
    last_name: Column = Column(
        String(50),
        nullable=True,
    )
    gender: Column = Column(
        SqlAlchemyEnum(UserGender),
        nullable=True,
    )
    birth_year: Column = Column(
        Integer,
        nullable=True,
    )
    email: Column = Column(
        String(50),
        unique=True,
        nullable=False,
    )
    hashed_password: Column = Column(
        String(50),
        nullable=True,
    )


# -- Pydantic Models -- #

class UserCreatePydanticSchema(PydanticBaseModel):
    first_name: typing.Optional[str]
    last_name: typing.Optional[str]
    gender: typing.Optional[UserGender]
    birth_year: typing.Optional[int]
    email: str
    banned_from_webapp: bool = False


class UserPydanticSchema(UserCreatePydanticSchema):
    id: int
