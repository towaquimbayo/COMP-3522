import abc


class Item(abc.ABC):
    def __init__(self, name, description, product_id):
        """
        Initializes the item.
        :param name: name of the item
        :param description: description of the item
        :param product_id: product id of the item
        """
        self.__name = name
        self.__description = description
        self.__product_id = product_id

    def get_name(self):
        """
        Returns the name of the item.
        :return: name of the item
        """
        return self.__name

    def set_name(self, name):
        """
        Sets the name of the item.
        :param name: name of the item
        """
        self.__name = name

    def get_description(self):
        """
        Returns the description of the item.
        :return: description of the item
        """
        return self.__description

    def set_description(self, description):
        """
        Sets the description of the item.
        :param description: description of the item
        """
        self.__description = description

    def get_product_id(self):
        """
        Returns the product id of the item.
        :return: product id of the item
        """
        return self.__product_id

    def set_product_id(self, product_id):
        """
        Sets the product id of the item.
        :param product_id: product id of the item
        """
        self.__product_id = product_id

    name = property(get_name, set_name)
    description = property(get_description, set_description)
    product_id = property(get_product_id, set_product_id)

    def __str__(self):
        """
        Returns a string representation of the item.
        :return: string representation of the item
        """
        return f"Item: {self.name}, Product ID: {self.product_id}"
