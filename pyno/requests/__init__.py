from pyno.models import Database, User
from pyno.requests.response_objects import DatabaseList, UserList
import json
from typing import Optional
import requests
from requests.models import Response
from ..utils import build_url
from os import environ as env


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

    def get(self, query: str) -> requests.Response:
        url = f'{self.__endpoint}/{query}'
        return requests.get(url, headers=self.__headers)

    def post(self, query: str, data: dict) -> requests.Response:
        url = f'{self.__endpoint}/{query}/query'
        hdrs = self.__headers.copy()
        hdrs.update({"Content-type": "application/json"})
        return requests.post(url, headers=hdrs, data=data)

    def request_data(self):
        return self.__endpoint, self.__headers

class NotionApi:
    @staticmethod
    def get_all_users(page_size: Optional[int] = None, start_cursor:
                      Optional[str] = None) -> Optional[UserList]:
        dbe = Endpoint('users')
        ep, hdrs = dbe.request_data()
        response: Optional[Response] = None
        if page_size:
            ep = add_query_param(ep, page_size=page_size)
        if start_cursor:
            ep = add_query_param(ep, start_cursor=start_cursor)
        response = requests.get(ep, headers=hdrs)
        if response.status_code != 200:
            raise ValueError
        data = json.loads(response.text)
        return UserList.parse_obj(data)

    @staticmethod
    def get_user(id: str) -> Optional[User]:
        dbe = Endpoint('users')
        ep, hdrs = dbe.request_data()
        response: Optional[Response] = None
        response = requests.get(f'{ep}/{id}', headers=hdrs)
        if response.status_code != 200:
            raise ValueError
        data = json.loads(response.text)
        return User(**data)

    @staticmethod
    def get_database(id: str) -> Optional[Database]:
        dbe = Endpoint('databases')
        ep, hdrs = dbe.request_data()
        response: Optional[Response] = None
        response = requests.get(f'{ep}/{id}', headers=hdrs)
        if response.status_code != 200:
            raise ValueError
        data = json.loads(response.text)
        return Database(**data)

    @staticmethod
    def list_databases() -> Optional[DatabaseList]:
        dbe = Endpoint('databases')
        ep, hdrs = dbe.request_data()
        response: Optional[Response] = None
        response = requests.get(ep, headers=hdrs)
        if response.status_code != 200:
            raise ValueError
        data = json.loads(response.text)
        return DatabaseList.parse_obj(data)

    # @staticmethod
    # def add_page_to_db(db_id, page: Page)
        

# curl -X POST https://api.notion.com/v1/pages \
#   -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
#   -H "Content-Type: application/json" \
#   -H "Notion-Version: 2021-05-13" \
#   --data '{
#       "parent": { "type": "database_id", "database_id": "2f26ee68-df30-4251-aad4-8ddc420cba3d" },
#       "properties": {
#       "Grocery item": {
#         "type": "title",
#         "title": [{ "type": "text", "text": { "content": "Tomatoes" } }]
#       },
#       "Price": {
#         "type": "number",
#         "number": 1.49
#       },
#       "Last ordered": {
#         "type": "date",
#         "date": { "start": "2021-05-11" }
#       }
#     }
#   }'