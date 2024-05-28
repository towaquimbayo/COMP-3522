from classes.candy import Candy


class CandyCanes(Candy):
    def __init__(self, name, description, product_id, has_nuts, has_lactose, color):
        """
        Initializes the candy canes.
        :param name: name of the candy canes
        :param description: description of the candy canes
        :param product_id: product id of the candy canes
        :param has_nuts: whether the candy canes have nuts
        :param has_lactose: whether the candy canes have lactose
        :param color: color of the candy canes
        """
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.__color = color

    def get_color(self):
        """
        Returns the color of the candy canes.
        :return: color of the candy canes
        """
        return self.__color

    def set_color(self, color):
        """
        Sets the color of the candy canes.
        :param color: color of the candy canes
        """
        self.__color = color

    color = property(get_color, set_color)
