from book import Book
from item_factory import ItemFactory


class BookItemFactory(ItemFactory):
    def create_item(self, **kwargs) -> Book:
        return Book(kwargs["title"], kwargs["call_number"], kwargs["num_of_copies"], kwargs["author"])
                      