from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

from ._user import User


@dataclass
class PropertyTypeEnum(str, Enum):
    CHECKBOX = "checkbox"
    CREATED_BY = "created_by"
    CREATED_TIME = "created_time"
    DATE = "date"
    EMAIL = "email"
    FILE = "file"
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
    TITLE = "title"
    URL = "url"


class Property(BaseModel):
    id: Optional[str]
    type: str


class Link(BaseModel):
    url: str
    type = 'url'


class Annotations(BaseModel):
    bold = False
    italic = False
    strikethrough = False
    underline = False
    code = False
    color = 'default'


class TextObject(BaseModel):
    content: str
    link: Optional[Link]


class EquationObject(BaseModel):
    expression: str


class MentionObject(BaseModel):
    type: str


class PageMentionObject(BaseModel):
    page: str


class DatabaseMentionObject(BaseModel):
    database: str


class DateProperty(BaseModel):
    start: datetime
    end: datetime


class DateMentionObject(BaseModel):
    date: DateProperty


class UserMentionObject(BaseModel):
    user: User


@dataclass
class RichTextTypeEnum(str, Enum):
    TEXT = "text"
    MENTION = "mention"
    EQUATION = "equation"


class RichText(BaseModel):
    plain_text: str
    href: Optional[str]
    annotations: Annotations
    type: str
    text: Optional[TextObject]
    mention: Optional[TextObject]
    equation: Optional[TextObject]


class Option(BaseModel):
    id: str
    name: str
    color: str
