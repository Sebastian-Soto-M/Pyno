from pydantic import BaseModel
from typing import List, NewType, Optional, Generic, TypeVar
from ..models import User, Database


DT = TypeVar('DT')

class ResponseListModel(BaseModel, Generic[DT]):
    object = 'list'
    results: List[DT]
    next_cursor: Optional[str]
    has_more = False

UserListModel = NewType('UserList', ResponseListModel[User])
DatabaseListModel = NewType('DatabaseList', ResponseListModel[Database])