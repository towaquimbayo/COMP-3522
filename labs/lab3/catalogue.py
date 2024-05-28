import difflib
from library_item_generator import LibraryItemGenerator


class Catalogue:
    def __init__(self):
        self.catalogue_list = []

    def add(self):
        item = LibraryItemGenerator.generate_item()
        if item is None:
            return
        if item not in self.catalogue_list:
            self.catalogue_list.append(item)

    def remove(self, call_number):
        for item in self.catalogue_list:
            if item.call_number == call_number:
                self.catalogue_list.remove(item)
                print(f"{item.get_item_instance()} with call number {call_number} removed.")
                return
        print(f"Item with call number {call_number} not found.")

    def find(self, string):
        found_items = []
        for item in self.catalogue_list:
            if string.lower() in item.title.lower():
                found_items.append(item)
        if not found_items:
            similar_titles = difflib.get_close_matches(string, [item.title for item in self.catalogue_list])
            if similar_titles:
                print(f"Item not found. Did you mean one of these titles? {', '.join(similar_titles)}")
            else:
                print("Item not found.")
        return found_items

    def check_out(self, call_number):
        for item in self.catalogue_list:
            if item.call_number == call_number:
                if item.check_availability():
                    item.num_of_copies -= 1
                    print(f"{item.get_item_instance()} with call number {call_number} checked out successfully.")
                    return
                else:
                    print(f"{item.get_item_instance()} with call number {call_number} is not available for check out.")
                    return
        print(f"Item with call number {call_number} not found.")

    def return_item(self, call_number):
        for item in self.catalogue_list:
            if item.call_number == call_number:
                item.num_of_copies += 1
                print(f"{item.get_item_instance()} with call number {call_number} returned successfully.")
                return
        print(f"Item with call number {call_number} not found.")

    def display_available_items(self):
        if not self.catalogue_list:
            print("No items available.")
        else:
            for item in self.catalogue_list:
                print("\n" + str(item))
