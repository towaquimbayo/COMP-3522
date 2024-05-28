from classes.item import Item


class Candy(Item):
    def __init__(self, name, description, product_id, has_nuts, has_lactose):
        """
        Initializes the candy.
        :param name: name of the candy
        :param description: description of the candy
        :param product_id: product id of the candy
        :param has_nuts: True if the candy has nuts, False otherwise
        :param has_lactose: True if the candy has lactose, False otherwise
        """
        super().__init__(name, description, product_id)
        self.__has_nuts = has_nuts
        self.__has_lactose = has_lactose

    def get_has_nuts(self):
        """
        Returns whether the candy has nuts.
        :return: True if the candy has nuts, False otherwise
        """
        return self.__has_nuts

    def set_has_nuts(self, has_nuts):
        """
        Sets whether the candy has nuts.
        :param has_nuts: True if the candy has nuts, False otherwise
        """
        self.__has_nuts = has_nuts

    def get_has_lactose(self):
        """
        Returns whether the candy has lactose.
        :return: True if the candy has lactose, False otherwise
        """
        return self.__has_lactose

    def set_has_lactose(self, has_lactose):
        """
        Sets whether the candy has lactose.
        :param has_lactose: True if the candy has lactose, False otherwise
        """
        self.__has_lactose = has_lactose

    has_nuts = property(get_has_nuts, set_has_nuts)
    has_lactose = property(get_has_lactose, set_has_lactose)
