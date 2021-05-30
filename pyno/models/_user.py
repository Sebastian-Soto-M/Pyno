from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


class UserTypeEnum(str, Enum):
    PERSON = "person"
    BOT = "bot"


class User(BaseModel):
    object = 'user'
    id: str
    type: UserTypeEnum
    name: Optional[str]
    avatar_url: Optional[str]


class Person(User):
    person = {"email": str}


class Bot(User):
    bot: dict
