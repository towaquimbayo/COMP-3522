from classes.stuffed_animal import StuffedAnimal


class Reindeer(StuffedAnimal):
    def __init__(self, name, description, product_id, stuffing, size, fabric, has_glow):
        """
        Initializes the reindeer.
        :param name: name of the reindeer
        :param description: description of the reindeer
        :param product_id: product id of the reindeer
        :param stuffing: stuffing of the reindeer
        :param size: size of the reindeer
        :param fabric: fabric of the reindeer
        :param has_glow: whether the reindeer has a glow
        """
        super().__init__(name, description, product_id, stuffing, size, fabric)
        self.__has_glow = has_glow

    def get_has_glow(self):
        """
        Returns whether the reindeer has a glow.
        :return: True if the reindeer has a glow, False otherwise
        """
        return self.__has_glow

    def set_has_glow(self, has_glow):
        """
        Sets whether the reindeer has a glow.
        :param has_glow: True if the reindeer has a glow, False otherwise
        """
        self.__has_glow = has_glow

    has_glow = property(get_has_glow, set_has_glow)
