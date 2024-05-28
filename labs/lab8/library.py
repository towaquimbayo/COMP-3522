from catalogue import Catalogue

"""
This file contains the Library class.

@Author: Muhammad Noufil Saqib
@Version: 1.0.0
"""


class Library:
    def __init__(self, item_list=None):
        self._catalogue = Catalogue(item_list) if item_list is not None else Catalogue()

    def add_item(self):
        """
        This function adds an item to the Catalogue in the library
        :return: None
        """
        self._catalogue.add_item()

    def remove_item(self, call_number):
        """
        This function removes an item from the Catalogue in the library
        :param call_number: the call number of the item to be removed
        :return: None
        """
        self._catalogue.remove_item(call_number)

    def find_items(self, title):
        """
        This function finds items in the Catalogue in the library
        :param title: the title of the item to be found
        :return: the list of items found
        """
        return self._catalogue.find_items(title)

    def check_out(self, call_number):
        """
        This function checks out an item from the Catalogue in the library
        :param call_number: the call number of the item to be checked out
        :return: None
        """
        item = self._catalogue.find_item_by_call_number(call_number)
        if item is None:
            print(f"Item with call number {call_number} not found.")
        else:
            if item.check_availability():
                item.remove_copy()
                print(f"Item with call number {call_number} checked out successfully.")
            else:
                print(f"Item with call number {call_number} is not available for check out.")

    def return_item(self, call_number):
        """
        This function returns an item to the Catalogue in the library
        :param call_number: the call number of the item to be returned
        :return: None
        """
        item = self._catalogue.find_item_by_call_number(call_number)
        if item is None:
            print(f"Item with call number {call_number} not found.")
        else:
            item.add_copy()
            print(f"Item with call number {call_number} returned successfully.")

    def display_available_items(self):
        """
        This function displays all the available items in the Catalogue in the library
        :return: None
        """
        items = self._catalogue.get_item_list()
        if not items:
            print("No items available.")
        else:
            print(*items, sep="\n\n")
