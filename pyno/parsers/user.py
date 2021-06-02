from typing import NewType, Union

from requests import Response

from ..models import BotModel, PersonModel, UserModel
from . import ResponseListModel

UserListModel = NewType('UserListModel', ResponseListModel[UserModel])


def specify(user: UserModel) -> Union[PersonModel, BotModel]:
    if 'bot' in user.keys():
        return BotModel(**user)
    return PersonModel(**user)


def parse_user(response: Response) -> Union[PersonModel, BotModel]:
    if response.ok:
        return specify(response.json())
    else:
        raise ValueError


def parse_user_list(response: Response) -> UserListModel:
    if response.ok:
        user_list = ResponseListModel[UserModel].parse_raw(response.text)
        for user in user_list.results:
            user = specify(user)
        return user_list
    else:
        raise ValueError
