from classes.candy import Candy


class CremeEggs(Candy):
    def __init__(self, name, description, product_id, has_nuts, has_lactose, pack_size):
        """
        Initializes the creme eggs.
        :param name: name of the creme eggs
        :param description: description of the creme eggs
        :param product_id: product id of the creme eggs
        :param has_nuts: True if the creme eggs has nuts, False otherwise
        :param has_lactose: True if the creme eggs has lactose, False otherwise
        :param pack_size: pack size of the creme eggs
        """
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.__pack_size = pack_size

    def get_pack_size(self):
        """
        Returns the pack size of the creme eggs.
        :return: pack size of the creme eggs
        """
        return self.__pack_size

    def set_pack_size(self, pack_size):
        """
        Sets the pack size of the creme eggs.
        :param pack_size: pack size of the creme eggs
        """
        self.__pack_size = pack_size

    pack_size = property(get_pack_size, set_pack_size)
