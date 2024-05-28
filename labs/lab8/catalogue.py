import difflib
from library_item_generator import LibraryItemGenerator

"""
This is the Catalogue module. It contains the Catalogue class that represents a catalogue in a library.

@Author: Muhammad Noufil Saqib
@Version: 1.0.0
"""


class Catalogue:
    def __init__(self, item_list=None):
        self._item_list = item_list if item_list is not None else []
        self._item_generator = LibraryItemGenerator()

    def get_item_list(self):
        """
        This function returns the list of items in the catalogue
        :return: the list of items in the catalogue
        """
        return self._item_list

    def find_item_by_call_number(self, call_number):
        """
        This function finds an item in the catalogue by call number
        :param call_number: the call number of the item to be found
        :return: the item found
        # """
        return next((item for item in self._item_list if item.call_number == call_number), None)

    def add_item(self):
        """
        This function adds an item to the catalogue
        :return: None
        """
        item = self._item_generator.generate()
        if self.find_item_by_call_number(item.call_number) is None:
            self._item_list.append(item)
            print(f"Item successfully added. Item info:\n{item}")
        else:
            print(f"Item with call number {item.call_number} already exists.")

    def remove_item(self, call_number):
        """
        This function removes an item from the catalogue
        :param call_number: the call number of the item to be removed
        :return: None
        """
        if self.find_item_by_call_number(call_number) is None:
            print(f"Item with call number {call_number} not found.")
        else:
            self._item_list.remove(self.find_item_by_call_number(call_number))
            print(f"Item with call number {call_number} removed.")

    def find_items(self, title):
        """
        This function finds items in the catalogue
        :param title: the title of the item to be found
        :return: the list of items found
        """
        found_items = [item for item in self._item_list if title.lower() in item.title.lower()]
        if not found_items:
            similar_titles = difflib.get_close_matches(title, [item.title for item in self._item_list])
            if similar_titles:
                print(f"Item not found. Did you mean one of these titles? {', '.join(similar_titles)}")
            else:
                print("Item not found.")
            return None
        return found_items
