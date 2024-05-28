from classes.candy import Candy


class PumpkinCaramelToffee(Candy):
    def __init__(self, name, description, product_id, has_nuts, has_lactose, variety):
        """
        Initializes the pumpkin caramel toffee.
        :param name: name of the pumpkin caramel toffee
        :param description: description of the pumpkin caramel toffee
        :param product_id: product id of the pumpkin caramel toffee
        :param has_nuts: True if the pumpkin caramel toffee has nuts, False otherwise
        :param has_lactose: True if the pumpkin caramel toffee has lactose, False otherwise
        :param variety: variety of the pumpkin caramel toffee
        """
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.__variety = variety

    def get_variety(self):
        """
        Returns the variety of the pumpkin caramel toffee.
        :return: variety of the pumpkin caramel toffee
        """
        return self.__variety

    def set_variety(self, variety):
        """
        Sets the variety of the pumpkin caramel toffee.
        :param variety: variety of the pumpkin caramel toffee
        """
        self.__variety = variety

    variety = property(get_variety, set_variety)
