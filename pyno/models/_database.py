from typing import List

from pydantic import BaseModel

from ._property import RichText


class Database(BaseModel):
    object = 'database'
    id: str
    created_time: str
    last_edited_time: str
    title: List[RichText]
    properties: dict
