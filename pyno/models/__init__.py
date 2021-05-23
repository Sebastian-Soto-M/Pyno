from pydantic import BaseModel, PrivateAttr
from pydantic.dataclasses import dataclass
from typing import Optional, List, Any, Dict, Type
from enum import Enum
from datetime import datetime


@dataclass
class UserTypeEnum(str, Enum):
    PERSON = "person"
    BOT = "bot"


class User(BaseModel):
    object: str
    id: str
    type: str
    person: Optional[dict]
    bot: Optional[dict]
    name: Optional[str]
    avatar_url: Optional[str]


class Link(BaseModel):
    url: str
    type = 'url'


@dataclass
class PropertyTypeEnum(str, Enum):
    TITLE = "title"
    RICH_TEXT = "rich_text"
    NUMBER = "number"
    SELECT = "select"
    MULTI_SELECT = "multi_select"
    DATE = "date"
    PEOPLE = "people"
    FILE = "file"
    CHECKBOX = "checkbox"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    FORMULA = "formula"
    RELATION = "relation"
    ROLLUP = "rollup"
    CREATED_TIME = "created_time"
    CREATED_BY = "created_by"
    LAST_EDITED_TIME = "last_edited_time"
    LAST_EDITED_BY = "last_edited_by"


class Property(BaseModel):
    id: str
    type: str


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


class Database(BaseModel):
    object = 'database'
    id: str
    created_time: str
    last_edited_time: str
    title: List[RichText]
    properties: Any


class Option(BaseModel):
    id: str
    name: str
    color: str
