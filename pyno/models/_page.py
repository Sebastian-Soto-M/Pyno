from typing import Dict

from pydantic import BaseModel


class PageModel(BaseModel):
    object = 'page'
    id: str
    created_time: str
    last_edited_time: str
    archived: bool
    properties: Dict[str, dict]


class CreatePageRequestModel(BaseModel):
    parent = {"database_id": str}
    properties: Dict[str, dict]
