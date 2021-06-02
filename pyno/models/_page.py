from typing import Dict, Optional

from pydantic import BaseModel


class PageParentModel(BaseModel):
    type = 'database_id'
    database_id: str


class CreatePageRequestModel(BaseModel):
    parent: PageParentModel
    properties: Dict[str, dict]


class PageModel(BaseModel):
    object = 'page'
    id: str
    created_time: str
    last_edited_time: str
    parent: Optional[PageParentModel]
    archived: bool
    properties: Dict[str, dict]
