from typing import Generic, List, NewType, Optional, TypeVar

from pydantic import BaseModel

from ..models import Database, User

DT = TypeVar('DT')


class ResponseListModel(BaseModel, Generic[DT]):
    object = 'list'
    results: List[DT]
    next_cursor: Optional[str]
    has_more = False


UserListModel = NewType('UserList', ResponseListModel[User])
DatabaseListModel = NewType('DatabaseList', ResponseListModel[Database])
