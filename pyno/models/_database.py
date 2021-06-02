import pdb
from datetime import datetime
from typing import Any, List, NewType

from pydantic import BaseModel, validator

from ._property import (NumberPropertyModel, PropertyModel, PropertyTypeEnum,
                        RichTextObjectModel, RichTextPropertyFactory,
                        RichTextPropertyModel, RichTextTypeEnum,
                        SelectPropertyModel, TitlePropertyModel)
from ._response import ResponseListModel


class DatabaseModel(BaseModel):
    object = 'database'
    id: str
    created_time: datetime
    last_edited_time: datetime
    title: List[RichTextObjectModel]
    properties: dict

    @validator('created_time', 'last_edited_time',  pre=True)
    def time_validate(cls, v):
        return datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%fZ')

    @validator('properties')
    def properties_validate(cls, v):
        for _, value in v.items():
            tp = PropertyTypeEnum(value['type'])
            value['type'] = tp
        return v


DatabaseListModel = NewType('DatabaseList', ResponseListModel[DatabaseModel])


class ColumnFactory:
    @staticmethod
    def set(property_type: PropertyTypeEnum, value: Any) -> PropertyModel:
        if property_type == PropertyTypeEnum.TITLE:
            if isinstance(value, str):
                rtp = RichTextPropertyFactory.get(
                    type=RichTextTypeEnum.TEXT, value=value)
                res = TitlePropertyModel(title=[rtp])
                return res
            return TitlePropertyModel(**value)
        if property_type == PropertyTypeEnum.SELECT:
            if isinstance(value, str):
                return SelectPropertyModel(select={'name': value})
            return SelectPropertyModel(**value)
        if property_type == PropertyTypeEnum.RICH_TEXT:
            if isinstance(value, str):
                return RichTextPropertyModel(rich_text=[RichTextPropertyFactory.get(
                    type=RichTextTypeEnum.TEXT, value=value)])
            return RichTextObjectModel(**value)
        if property_type == PropertyTypeEnum.NUMBER:
            if not isinstance(value, dict):
                try:
                    value = int(value)
                except ValueError:
                    value = float(value)
                return NumberPropertyModel(number=value)
            return NumberPropertyModel(**value)
