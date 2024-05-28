from dvd import DVD
from item_factory import ItemFactory


class DVDItemFactory(ItemFactory):
    def create_item(self, **kwargs) -> DVD:
        return DVD(kwargs["title"], kwargs["call_number"], kwargs["num_of_copies"], kwargs["release_date"],
                   kwargs["region_code"])
