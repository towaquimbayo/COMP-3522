class Order:
    def __init__(
        self,
        order_number,
        product_id,
        quantity,
        item_type,
        name,
        product_details,
        item_factory,
    ):
        """
        Creates an Order object.
        :param order_number: order number
        :param product_id: product ID
        :param quantity: quantity
        :param item_type: item type
        :param name: item name
        :param product_details: product details as a dictionary
        :param item_factory: item factory
        """
        self.__order_number = order_number
        self.__product_id = product_id
        self.__quantity = quantity
        self.__item_type = item_type
        self.__name = name
        self.__product_details = product_details
        self.__item_factory = item_factory

    def get_order_number(self):
        """
        Returns the order number.
        :return: order number
        """
        return self.__order_number

    def set_order_number(self, order_number):
        """
        Sets the order number.
        :param order_number: order number
        """
        self.__order_number = order_number

    def get_product_id(self):
        """
        Returns the product ID.
        :return: product ID
        """
        return self.__product_id

    def set_product_id(self, product_id):
        """
        Sets the product ID.
        :param product_id: product ID
        """
        self.__product_id = product_id

    def get_quantity(self):
        """
        Returns the quantity.
        :return: quantity
        """
        return self.__quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity.
        :param quantity: quantity
        """
        self.__quantity = quantity

    def get_item_type(self):
        """
        Returns the item type.
        :return: item type
        """
        return self.__item_type

    def set_item_type(self, item_type):
        """
        Sets the item type.
        :param item_type: item type
        """
        self.__item_type = item_type

    def get_name(self):
        """
        Returns the name.
        :return: item name
        """
        return self.__name

    def set_name(self, name):
        """
        Sets the name.
        :param name: item name
        """
        self.__name = name

    def get_product_details(self):
        """
        Returns the product details.
        :return: product details as a dictionary
        """
        return self.__product_details

    def set_product_details(self, product_details):
        """
        Sets the product details.
        :param product_details: product details as a dictionary
        """
        self.__product_details = product_details

    def get_item_factory(self):
        """
        Returns the item factory.
        :return: item factory
        """
        return self.__item_factory

    def set_item_factory(self, item_factory):
        """
        Sets the item factory.
        :param item_factory: item factory
        """
        self.__item_factory = item_factory

    order_number = property(get_order_number, set_order_number)
    product_id = property(get_product_id, set_product_id)
    quantity = property(get_quantity, set_quantity)
    item_type = property(get_item_type, set_item_type)
    name = property(get_name, set_name)
    product_details = property(get_product_details)
    item_factory = property(get_item_factory, set_item_factory)
