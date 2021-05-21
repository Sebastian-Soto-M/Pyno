from typing import List
import pdb
from functools import cached_property
import requests
from . import TOKEN, URL
from .models.columns import ColumnFactory, Column
from .utils import build_url
import json

DEFAULT_TIMEOUT = 5  # seconds
DATABASE_ID = "5f7f1bcdfff04414ac5cd7099b871726"


def print_json(data):
    print(json.dumps(data, indent=4))


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


class NotionApi():
    @staticmethod
    def query_database(id: str, filter={}, sort={}) -> list:
        dbe = Endpoint('databases')
        try:
            data = {}
            res = dbe.post(id, data)
            if res.status_code != 200:
                raise ValueError
            else:
                return json.loads(res.text)['results']
        except ValueError:
            return []

    @staticmethod
    def get_database(id: str):
        dbe = Endpoint('databases')
        try:
            res = dbe.get(id)
            if res.status_code != 200:
                raise ValueError
            else:
                return json.loads(res.text)
        except ValueError:
            return {}


class Database():
    def __init__(self, id: str):
        self.__res = NotionApi().get_database(id)
        self.__id = id
        self.__title = ""
        self.__columns = []
        if len(self.__res.keys()) > 0:
            self.__title = self.__res['title'][0]['plain_text']

    @cached_property
    def columns(self) -> List[Column]:
        cols = []
        for k, v in self.__res['properties'].items():
            col = ColumnFactory().get_column(column_type=v['type'], title=k)
            col.init_data(v)
            cols.append(col)
        return cols

    @property
    def id(self) -> str:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    def query(self, filter: dict = {}, sort: dict = {}) -> list:
        return NotionApi.query_database(self.__id, filter=filter, sort=sort)

    def load_columns(self, data: list):
        for row in data:
            prop = row['properties']
            for k, v in prop.items():
                for col in self.columns:
                    if col.id == v['id']:
                        col.add_value(v)


db = Database(DATABASE_ID)
db.load_columns(db.query())
for col in db.columns:
    print(col.title, col.values)
