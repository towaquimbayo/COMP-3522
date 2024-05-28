from classes.item import Item


class StuffedAnimal(Item):
    def __init__(self, name, description, product_id, stuffing, size, fabric):
        """
        Initializes the stuffed animal.
        :param name: name of the stuffed animal
        :param description: description of the stuffed animal
        :param product_id: product id of the stuffed animal
        :param stuffing: stuffing of the stuffed animal
        :param size: size of the stuffed animal
        :param fabric: fabric of the stuffed animal
        """
        super().__init__(name, description, product_id)
        self.__stuffing = stuffing
        self.__size = size
        self.__fabric = fabric

    def get_stuffing(self):
        """
        Returns the stuffing of the stuffed animal.
        :return: stuffing of the stuffed animal
        """
        return self.__stuffing

    def set_stuffing(self, stuffing):
        """
        Sets the stuffing of the stuffed animal.
        :param stuffing: stuffing of the stuffed animal
        """
        self.__stuffing = stuffing

    def get_size(self):
        """
        Returns the size of the stuffed animal.
        :return: size of the stuffed animal
        """
        return self.__size

    def set_size(self, size):
        """
        Sets the size of the stuffed animal.
        :param size: size of the stuffed animal
        """
        self.__size = size

    def get_fabric(self):
        """
        Returns the fabric of the stuffed animal.
        :return: fabric of the stuffed animal
        """
        return self.__fabric

    def set_fabric(self, fabric):
        """
        Sets the fabric of the stuffed animal.
        :param fabric: fabric of the stuffed animal
        """
        self.__fabric = fabric

    stuffing = property(get_stuffing, set_stuffing)
    size = property(get_size, set_size)
    fabric = property(get_fabric, set_fabric)
