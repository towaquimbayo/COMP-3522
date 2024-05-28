from classes.toys import Toys


class SantaWorkshop(Toys):
    def __init__(
        self,
        name,
        description,
        product_id,
        has_batteries,
        min_age,
        dimensions,
        num_rooms,
    ):
        """
        Initializes the Santa Workshop.
        :param name: name of the Santa Workshop
        :param description: description of the Santa Workshop
        :param product_id: product id of the Santa Workshop
        :param has_batteries: whether the Santa Workshop has batteries
        :param min_age: minimum age of the Santa Workshop
        :param dimensions: dimensions of the Santa Workshop
        :param num_rooms: number of rooms in the Santa Workshop
        """
        super().__init__(name, description, product_id, has_batteries, min_age)
        self.__dimensions = dimensions
        self.__num_rooms = num_rooms

    def get_dimensions(self):
        """
        Returns the dimensions of the Santa Workshop.
        :return: dimensions of the Santa Workshop
        """
        return self.__dimensions

    def set_dimensions(self, dimensions):
        """
        Sets the dimensions of the Santa Workshop.
        :param dimensions: dimensions of the Santa Workshop
        """
        self.__dimensions = dimensions

    def get_num_rooms(self):
        """
        Returns the number of rooms in the Santa Workshop.
        :return: number of rooms in the Santa Workshop
        """
        return self.__num_rooms

    def set_num_rooms(self, num_rooms):
        """
        Sets the number of rooms in the Santa Workshop.
        :param num_rooms: number of rooms in the Santa Workshop
        """
        self.__num_rooms = num_rooms

    dimensions = property(get_dimensions, set_dimensions)
    num_rooms = property(get_num_rooms, set_num_rooms)
