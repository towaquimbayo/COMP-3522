import abc

from classes.candy import Candy
from classes.stuffed_animal import StuffedAnimal
from classes.toys import Toys


class ItemFactory(abc.ABC):
    """
    Abstract class for item factory
    """

    @abc.abstractmethod
    def create_toys(self, name, product_details, product_id) -> Toys:
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, name, product_details, product_id) -> StuffedAnimal:
        pass

    @abc.abstractmethod
    def create_candy(self, name, product_details, product_id) -> Candy:
        pass
