import pdb
from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel, validator

from ._property import PropertyTypeEnum, RichText


class Column(BaseModel):
    type: str


class Database(BaseModel):
    object = 'database'
    id: str
    created_time: datetime
    last_edited_time: datetime
    title: List[RichText]
    properties: dict

    @validator('created_time', 'last_edited_time',  pre=True)
    def time_validate(cls, v):
        return datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%fZ')

    @validator('properties')
    def properties_validate(cls, v):
        for _, value in v.items():
            tp = PropertyTypeEnum(value['type'])
            value['type'] = tp
        return v
