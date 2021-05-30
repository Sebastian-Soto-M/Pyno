import logging
import time
from functools import wraps
from typing import Generic, List, Optional, TypeVar

from pydantic.main import BaseModel
from requests import Response

DT = TypeVar('DT')


class ResponseListModel(BaseModel, Generic[DT]):
    object = 'list'
    results: List[DT]
    next_cursor: Optional[str]
    has_more = False
