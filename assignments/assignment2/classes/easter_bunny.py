from classes.stuffed_animal import StuffedAnimal


class EasterBunny(StuffedAnimal):
    def __init__(self, name, description, product_id, stuffing, size, fabric, color):
        """
        Initializes the Easter bunny.
        :param name: name of the Easter bunny
        :param description: description of the Easter bunny
        :param product_id: product id of the Easter bunny
        :param stuffing: stuffing of the Easter bunny
        :param size: size of the Easter bunny
        :param fabric: fabric of the Easter bunny
        :param color: color of the Easter bunny
        """
        super().__init__(
            name,
            description,
            product_id,
            stuffing,
            size,
            fabric,
        )
        self.__color = color

    def get_color(self):
        """
        Returns the color of the Easter bunny.
        :return: color of the Easter bunny
        """
        return self.__color

    def set_color(self, color):
        """
        Sets the color of the Easter bunny.
        :param color: color of the Easter bunny
        """
        self.__color = color

    color = property(get_color, set_color)
