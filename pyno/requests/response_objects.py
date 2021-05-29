from pydantic import BaseModel
from typing import List, NewType, Optional, Generic, TypeVar
from ..models import User, Database


DT = TypeVar('DT')

class ResponseList(BaseModel, Generic[DT]):
    object = 'list'
    results: List[DT]
    next_cursor: Optional[str]
    has_more = False

UserList = NewType('UserList', ResponseList[User])
DatabaseList = NewType('DatabaseList', ResponseList[Database])