import json
from typing import NewType, Union

from requests import Response

from ..models import Database
from . import ResponseListModel

DatabaseListModel = NewType('DatabaseListModel', ResponseListModel[Database])


def parse_database(response: Response) -> Database:
    if response.ok:
        return Database.parse_obj(response.json())
    else:
        raise ValueError


def parse_database_list(response: Response) -> DatabaseListModel:
    if response.ok:
        db_list = ResponseListModel[Database].parse_obj(response.json())
        db_list.results = [Database.parse_obj(db) for db in db_list.results]
        return db_list
    else:
        raise ValueError
