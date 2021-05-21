from .enums import Color


class Option():
    def __init__(self, id: str, name: str, color: str):
        self.__id = id
        self.__name = name
        self.__color = color

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    def __repr__(self):
        return f'Name={self.name} ({self.color})'
