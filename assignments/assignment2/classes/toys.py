from classes.item import Item


class Toys(Item):
    def __init__(self, name, description, product_id, has_batteries, min_age):
        """
        Initializes the toy.
        :param name: name of the toy
        :param description: description of the toy
        :param product_id: product id of the toy
        :param has_batteries: True if the toy has batteries, False otherwise
        :param min_age: minimum age of the toy
        """
        super().__init__(name, description, product_id)
        self.__has_batteries = has_batteries
        self.__min_age = min_age

    def get_has_batteries(self):
        """
        Returns whether the toy has batteries.
        :return: True if the toy has batteries, False otherwise
        """
        return self.__has_batteries

    def set_has_batteries(self, has_batteries):
        """
        Sets whether the toy has batteries.
        :param has_batteries: True if the toy has batteries, False otherwise
        """
        self.__has_batteries = has_batteries

    def get_min_age(self):
        """
        Returns the minimum age of the toy.
        :return: minimum age of the toy
        """
        return self.__min_age

    def set_min_age(self, min_age):
        """
        Sets the minimum age of the toy.
        :param min_age: minimum age of the toy
        """
        self.__min_age = min_age

    has_batteries = property(get_has_batteries, set_has_batteries)
    min_age = property(get_min_age, set_min_age)
