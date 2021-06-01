from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel

DT = TypeVar('DT')


class ResponseListModel(BaseModel, Generic[DT]):
    object = 'list'
    results: List[DT]
    next_cursor: Optional[str]
    has_more = False
