import pdb
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

from ._user import UserModel


class PropertyTypeEnum(str, Enum):
    CHECKBOX = "checkbox"
    CREATED_BY = "created_by"
    CREATED_TIME = "created_time"
    DATE = "date"
    EMAIL = "email"
    FILES = "files"
    FORMULA = "formula"
    LAST_EDITED_BY = "last_edited_by"
    LAST_EDITED_TIME = "last_edited_time"
    MULTI_SELECT = "multi_select"
    NUMBER = "number"
    PEOPLE = "people"
    PHONE_NUMBER = "phone_number"
    RELATION = "relation"
    RICH_TEXT = "rich_text"
    ROLLUP = "rollup"
    SELECT = "select"
    TEXT = "text"
    TITLE = "title"
    URL = "url"


class PropertyModel(BaseModel):
    id: Optional[str]
    type: PropertyTypeEnum


class LinkObjectModel(BaseModel):
    type = 'url'
    url: str


class AnnotationsModel(BaseModel):
    bold = False
    italic = False
    strikethrough = False
    underline = False
    code = False
    color = 'default'


class RichTextTypeEnum(str, Enum):
    TEXT = "text"
    MENTION = "mention"
    EQUATION = "equation"


class RichTextObjectModel(BaseModel):
    plain_text: Optional[str]
    href: Optional[str]
    annotations: AnnotationsModel = AnnotationsModel
    type: RichTextTypeEnum


class TextObjectModel(RichTextObjectModel):
    type = RichTextTypeEnum.TEXT
    text = {
        'content': str,
        'link': Optional[LinkObjectModel]
    }


class TitlePropertyModel(PropertyModel):
    type = PropertyTypeEnum.TITLE
    title: List[RichTextObjectModel]


class RichTextPropertyModel(BaseModel):
    rich_text: List[RichTextObjectModel]


class SelectPropertyModel(PropertyModel):
    type = PropertyTypeEnum.SELECT
    select = {
        'name': str
    }


class NumberPropertyModel(PropertyModel):
    type = PropertyTypeEnum.NUMBER
    number: Union[float, int]

# TODO update this factory


class RichTextPropertyFactory:
    @staticmethod
    def get(type: RichTextTypeEnum, value: Any):
        if type == RichTextTypeEnum.TEXT:
            if isinstance(value, str):
                return TextObjectModel(text={'content': value})
            return TextObjectModel(**value)
        if type == RichTextTypeEnum.MENTION:
            return TextObjectModel(**value)
        if type == RichTextTypeEnum.EQUATION:
            return TextObjectModel(**value)
