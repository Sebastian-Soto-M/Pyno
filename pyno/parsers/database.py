from typing import NewType, Union

from requests import Response

from ..models import DatabaseModel
from . import ResponseListModel

DatabaseListModel = NewType(
    'DatabaseListModel', ResponseListModel[DatabaseModel])


def parse_database(response: Response) -> DatabaseModel:
    if response.ok:
        return DatabaseModel.parse_raw(response.text)
    else:
        raise ValueError


def parse_database_list(response: Response) -> DatabaseListModel:
    if response.ok:
        db_list = ResponseListModel[DatabaseModel].parse_raw(response.text)
        db_list.results = [db for db in db_list.results]
        return db_list
    else:
        raise ValueError
