from enum import Enum
from typing import NewType, Optional

from pydantic import BaseModel

from ._response import ResponseListModel


class UserTypeEnum(str, Enum):
    PERSON = "person"
    BOT = "bot"


class UserModel(BaseModel):
    object = 'user'
    id: str
    type: UserTypeEnum
    name: Optional[str]
    avatar_url: Optional[str]


class PersonModel(UserModel):
    person = {"email": str}


class BotModel(UserModel):
    bot: dict


UserListModel = NewType('UserList', ResponseListModel[UserModel])
