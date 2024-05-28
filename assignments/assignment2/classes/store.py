from datetime import datetime
from exceptions.invalid_data_error import InvalidDataError


class Store:
    def __init__(self):
        """
        Creates a Store object.
        """
        self.__inventory = {}
        self.__orders = []
        self.__items_report = ""

    def get_inventory(self):
        """
        Returns the inventory.
        :return: dictionary of items
        """
        return self.__inventory

    def set_inventory(self, inventory):
        """
        Sets the inventory.
        :param inventory: dictionary of items
        """
        self.__inventory = inventory

    def get_orders(self):
        """
        Returns the orders.
        :return: list of orders
        """
        return self.__orders

    def set_orders(self, orders):
        """
        Sets the orders.
        :param orders: list of orders
        """
        self.__orders = orders

    def get_items_report(self):
        """
        Returns the items report.
        :return: string
        """
        return self.__items_report

    def set_items_report(self, items_report):
        """
        Sets the items report.
        :param items_report: string
        """
        self.__items_report = items_report

    inventory = property(get_inventory, set_inventory)
    orders = property(get_orders, set_orders)
    items_report = property(get_items_report, set_items_report)

    def create_daily_transaction_report(self):
        """
        Creates the daily transaction report.
        :return: report as a string
        """
        report = "HOLIDAY STORE - DAILY TRANSACTION REPORT (DTR)\n"
        report += f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
        report += self.items_report
        return report

    def process_order(self, order):
        """
        Finds the item in the inventory and reduces the stock.
        :param order: Order object
        """
        self.orders.append(order)

        # Add item to inventory if it doesn't exist
        if order.name not in [item.name for item in self.inventory.keys()]:
            try:
                self.__get_item_from_factory(order)
                self.items_report += (
                    f"Order {order.order_number}, Item {order.item_type}, Product ID {order.product_id}, "
                    f'Name "{order.name}", Quantity {order.quantity}\n'
                )
            except InvalidDataError as e:
                self.items_report += (
                    f"Order {order.order_number}, Could not process order data was corrupted, "
                    f"InvalidDataError - {e}\n"
                )
            except Exception as e:
                raise e

        # Reduce stock of item
        for item in self.inventory.keys():
            if item.name == order.name:
                # Restock if order quantity is greater than inventory
                if order.quantity > self.inventory[item]:
                    self.__restock_inventory(item)
                self.inventory[item] -= order.quantity

    def __get_item_from_factory(self, order):
        """
        Gets an item from the factory and adds it to the inventory.
        :param order: Order object
        """
        item = None
        if order.item_type.lower() == "toy":
            item = order.item_factory.create_toys(
                order.name,
                order.product_details,
                order.product_id,
            )
        elif order.item_type.lower() == "candy":
            item = order.item_factory.create_candy(
                order.name,
                order.product_details,
                order.product_id,
            )
        elif order.item_type.lower() == "stuffedanimal":
            item = order.item_factory.create_stuffed_animal(
                order.name,
                order.product_details,
                order.product_id,
            )
        if item is None:
            raise InvalidDataError(
                f"Item type {order.item_type} is not valid. Please check the order file."
            )
        self.inventory[item] = 100

    def __restock_inventory(self, item):
        """
        Restocks the inventory with 100 items.
        :param item: Store item
        """
        self.inventory[item] += 100
