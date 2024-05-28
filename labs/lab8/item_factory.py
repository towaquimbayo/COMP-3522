import abc
from item import Item


class ItemFactory(abc.ABC):
    @abc.abstractmethod
    def create_item(self, **kwargs) -> Item:
        pass

