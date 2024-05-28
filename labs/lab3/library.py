from catalogue import Catalogue


class Library:
    def __init__(self):
        self.catalogue = Catalogue()  # Composition

    def find_items(self, string):
        return self.catalogue.find(string)

    def add_item(self):
        self.catalogue.add()

    def remove_item(self, call_number):
        self.catalogue.remove(call_number)

    def check_out(self, call_number):
        self.catalogue.check_out(call_number)

    def return_item(self, call_number):
        self.catalogue.return_item(call_number)

    def display_available_items(self):
        self.catalogue.display_available_items()
