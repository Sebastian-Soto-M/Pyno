import json
from typing import NewType, Union

from requests import Response

from ..models import Bot, Person, User, UserMentionObject, UserTypeEnum
from . import ResponseListModel

UserListModel = NewType('UserList', ResponseListModel[User])


def specify(user: User) -> Union[Person, Bot]:
    if 'bot' in user.keys():
        return Bot(**user)
    return Person(**user)


def parse_user(response: Response) -> Union[Person, Bot]:
    if response.ok:
        return specify(response.json())
    else:
        raise ValueError


def parse_user_list(response: Response) -> UserListModel:
    if response.ok:
        user_list = ResponseListModel[User].parse_obj(response.json())
        for user in user_list.results:
            user = specify(user)
        return user_list
    else:
        raise ValueError
