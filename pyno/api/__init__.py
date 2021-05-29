import json
import pdb
from functools import wraps
from os import environ as env
from typing import Optional

import requests
from pydantic.main import BaseModel
from pyno.api.request import CreatePageRequestModel
from pyno.api.response import (DatabaseListModel, ResponseListModel,
                               UserListModel)
from pyno.models import Database, Page, User
from requests.models import Response

from ..utils import build_url

TOKEN = env['TOKEN']

URL = 'https://api.notion.com/v1/'


def add_query_param(url: str, **params) -> str:
    for k, v in params.items():
        param = f'?{k}={v}'
        url = url + param
    return url


class Endpoint():
    def __init__(self, endpoint: str):
        self.__endpoint = build_url(URL, endpoint)
        self.__headers = {
            "Authorization": "Bearer {0}".format(TOKEN),
            "Notion-Version": "2021-05-13"
        }

    def get(self, query: str) -> Response:
        url = f'{self.__endpoint}/{query}'
        return requests.get(url, headers=self.__headers)

    def post(self, query: str, data: dict) -> Response:
        url = f'{self.__endpoint}/{query}/query'
        hdrs = self.__headers.copy()
        hdrs.update({"Content-type": "application/json"})
        return requests.post(url, headers=hdrs, data=data)

    def request_data(self):
        return self.__endpoint, self.__headers


def endpoint(target: str):
    def inner_function(func):
        @wraps(func)
        def setup(*args):
            dbe = Endpoint(target)
            endpoint, headers = dbe.request_data()
            return func(*args, endpoint=endpoint, headers=headers)
        return setup
    return inner_function

class NotionApi:

    @staticmethod
    @endpoint('users')
    def get_user(id: str, endpoint: str, headers: dict) -> Optional[User]:
        response: Optional[Response] = requests.get(
            f'{endpoint}/{id}', headers=headers)
        if response.status_code != 200:
            raise ValueError
        data = json.loads(response.text)
        return User(**data)

    @staticmethod
    @endpoint('databases')
    def get_database(id: str, endpoint: str, headers: dict) -> Optional[Database]:
        response: Optional[Response] = None
        response = requests.get(f'{endpoint}/{id}', headers=headers)
        if response.status_code != 200:
            raise ValueError
        data = json.loads(response.text)
        return Database(**data)

    @staticmethod
    @endpoint('users')
    def get_all_users(endpoint: str,
                      headers: dict,
                      page_size: Optional[int] = None,
                      start_cursor: Optional[str] = None) -> Optional[UserListModel]:
        if page_size:
            endpoint = add_query_param(endpoint, page_size=page_size)
        if start_cursor:
            endpoint = add_query_param(endpoint, start_cursor=start_cursor)
        response: Optional[Response] = requests.get(endpoint, headers=headers)
        if response.status_code != 200:
            raise ValueError
        data = json.loads(response.text)
        return ResponseListModel[User].parse_obj(data)

    @staticmethod
    @endpoint('databases')
    def get_all_databases(endpoint: str, headers: dict) -> Optional[DatabaseListModel]:
        response: Optional[Response] = requests.get(endpoint, headers=headers)
        if not response.ok:
            raise ValueError
        data = json.loads(response.text)
        return ResponseListModel[Database].parse_obj(data)

    @staticmethod
    @endpoint('pages')
    def add_page_to_db(db_id, properties: dict, endpoint: str, headers: dict):
        data = {
            "parent": {"type": "database_id", "database_id": db_id},
            "properties": properties
        }
        data = CreatePageRequestModel(**data).dict()
        response: Optional[Response] = requests.post(
            endpoint, json=data, headers=headers)
        if not response.ok:
            raise ValueError
        return json.loads(response.text)
