from journal import Journal
from item_factory import ItemFactory


class JournalItemFactory(ItemFactory):
    def create_item(self, **kwargs) -> Journal:
        return Journal(kwargs["title"], kwargs["call_number"], kwargs["num_of_copies"], kwargs["author"],
                       kwargs["issue_number"], kwargs["publisher"])
