from os import environ as env
from typing import Dict, Optional, Tuple

import requests
from pyno.models import CreatePageRequestModel, PropertyModel
from requests.models import Response

TOKEN = env['TOKEN']

URL = 'https://api.notion.com/v1'


def add_query_param(url: str, **params) -> str:
    for k, v in params.items():
        param = f'?{k}={v}'
        url = url + param
    return url


class Endpoint():
    def __init__(self, endpoint: str):
        self.__endpoint = '/'.join([URL, endpoint])
        self.__headers = {
            "Authorization": "Bearer {0}".format(TOKEN),
            "Notion-Version": "2021-05-13"
        }

    @property
    def request_data(self):
        return self.__endpoint, self.__headers


def get_request_info(target: str) -> Tuple[str, dict]:
    return Endpoint(target).request_data


class NotionApi:

    @staticmethod
    def get_user(id: str) -> Response:
        endpoint, headers = get_request_info('users')
        return requests.get(f'{endpoint}/{id}', headers=headers)

    @staticmethod
    def get_all_users(page_size: Optional[int] = None, start_cursor: Optional[str] = None) -> Response:
        endpoint, headers = get_request_info('users')
        if page_size:
            endpoint = add_query_param(endpoint, page_size=page_size)
        if start_cursor:
            endpoint = add_query_param(endpoint, start_cursor=start_cursor)
        return requests.get(endpoint, headers=headers)

    @staticmethod
    def get_database(id: str) -> Response:
        endpoint, headers = get_request_info('databases')
        return requests.get(f'{endpoint}/{id}', headers=headers)

    @staticmethod
    def get_all_databases() -> Response:
        endpoint, headers = get_request_info('databases')
        return requests.get(endpoint, headers=headers)

    @staticmethod
    def add_page_to_db(db_id, properties: Dict[str, PropertyModel]) -> Response:
        endpoint, headers = get_request_info('pages')
        data = {
            "parent": {"type": "database_id", "database_id": db_id},
            "properties": properties
        }
        return requests.post(endpoint, json=CreatePageRequestModel(**data).dict(), headers=headers)
