from typing import Dict

from pydantic import BaseModel


class Page(BaseModel):
    object = 'page'
    id: str
    created_time: str
    last_edited_time: str
    archived: bool
    properties: Dict[str, dict]
