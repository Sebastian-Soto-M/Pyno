from abc import ABC, abstractmethod
from typing import Set
from . import Option
from enum import Enum


class ColumnType(Enum):
    CREATED_TIME = "created_time"
    MULTI_SELECT = "multi_select"
    NUMBER = "number"
    RICH_TEXT = "rich_text"
    SELECT = "select"
    TITLE = "title"


class Column(ABC):
    def __init__(self, id: str = "", title: str = ""):
        self._id = id
        self._title = title
        self._values = []

    @property
    def id(self) -> str: return self._id

    @property
    def title(self) -> str: return self._title

    @property
    @abstractmethod
    def details(self) -> str:
        pass

    @abstractmethod
    def add_value(self, val):
        pass

    @property
    def values(self):
        return self._values

    @abstractmethod
    def init_data(self, data: dict):
        raise NotImplementedError


class MultiSelect(Column):
    def __init__(self, id="", title=""):
        super().__init__(id, title)
        self.__options = Set[Option]

    @property
    def details(self):
        return f'{self.title}: Options = {self.__options}'

    def init_data(self, data: dict):
        self._id = data['id']
        self.__options = {Option(o['id'], o['name'], o['color']) for o in
                          data['multi_select']['options']}

    def add_value(self, val):
        opts = val['multi_select']
        self._values.append([Option(o['id'], o['name'], o['color']) for o in
                             opts])


class Select(Column):
    def __init__(self, id="", title=""):
        super().__init__(id, title)
        self.__options = Set[Option]

    @property
    def details(self):
        return f'{self.title}: Options = {self.__options}'

    def init_data(self, data: dict):
        self._id = data['id']
        self.__options = {Option(o['id'], o['name'], o['color']) for o in
                          data['select']['options']}

    def add_value(self, val):
        o = val['select']
        self._values.append(Option(o['id'], o['name'], o['color']))


class Number(Column):
    @property
    def details(self):
        return "I'm a number"

    def init_data(self, data: dict):
        self._id = data['id']

    def add_value(self, val):
        self._values.append(val['number'])


class CreatedTime(Column):
    @property
    def details(self):
        return "I'm a date"

    def init_data(self, data: dict):
        self._id = data['id']

    def add_value(self, val):
        self._values.append(val['created_time'])


class RichText(Column):
    @property
    def details(self):
        return "I'm text"

    def init_data(self, data: dict):
        self._id = data['id']

    def add_value(self, val):
        text = val['rich_text']
        for t in text:
            self._values.append(t['text']['content'])


class Title(Column):
    @property
    def details(self):
        return "I'm a title"

    def init_data(self, data: dict):
        self._id = data['id']

    def add_value(self, val):
        self._values.append(val['title'])


class ColumnFactory():
    @staticmethod
    def get_column(column_type: str, title: str):
        if column_type == ColumnType.CREATED_TIME.value:
            return CreatedTime(title=title)

        if column_type == ColumnType.MULTI_SELECT.value:
            return MultiSelect(title=title)

        if column_type == ColumnType.NUMBER.value:
            return Number(title=title)

        if column_type == ColumnType.RICH_TEXT.value:
            return RichText(title=title)

        if column_type == ColumnType.SELECT.value:
            return Select(title=title)

        if column_type == ColumnType.TITLE.value:
            return Title(title=title)
