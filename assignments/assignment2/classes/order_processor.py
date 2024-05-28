import pandas as pd
from classes.order import Order
from classes.christmas_item_factory import ChristmasItemFactory
from classes.halloween_item_factory import HalloweenItemFactory
from classes.easter_item_factory import EasterItemFactory


class OrderProcessor:
    """
    Reads each row of the order file and yields an Order object.
    """

    def __init__(self, order_filename):
        """
        Creates an OrderProcessor object.
        :param order_filename: order filename
        """
        self.__order_filename = order_filename
        self.__orders = self.__create_orders()

    def get_orders(self):
        """
        Returns the orders.
        :return: list
        """
        return self.__orders

    def __create_orders(self):
        """
        Reads each row of the order file and yields a list of Order objects.
        :return: list of Order objects
        """
        orders = []
        df = pd.read_excel(self.__order_filename)
        for index, row in df.iterrows():
            order_number = row["order_number"]
            holiday = row["holiday"].lower()
            item_type = row["item"]
            name = row["name"]
            quantity = row["quantity"]
            product_id = row["product_id"]
            product_details = {
                "description": row["description"],
                "has_batteries": row["has_batteries"],
                "min_age": row["min_age"],
                "dimensions": row["dimensions"],
                "num_rooms": row["num_rooms"],
                "speed": row["speed"],
                "jump_height": row["jump_height"],
                "has_glow": row["has_glow"],
                "spider_type": row["spider_type"],
                "num_sound": row["num_sound"],
                "colour": row["colour"],
                "has_lactose": row["has_lactose"],
                "has_nuts": row["has_nuts"],
                "variety": row["variety"],
                "pack_size": row["pack_size"],
                "stuffing": row["stuffing"],
                "size": row["size"],
                "fabric": row["fabric"],
            }

            if holiday == "christmas":
                item_factory = ChristmasItemFactory()
            elif holiday == "halloween":
                item_factory = HalloweenItemFactory()
            elif holiday == "easter":
                item_factory = EasterItemFactory()
            else:
                continue

            order = Order(
                order_number,
                product_id,
                quantity,
                item_type,
                name,
                product_details,
                item_factory,
            )
            orders.append(order)
        return orders
