from classes.item_factory import ItemFactory
from classes.santa_workshop import SantaWorkshop
from classes.reindeer import Reindeer
from classes.candy_canes import CandyCanes
from enums.candy_cane_colors import CandyCaneColors
from enums.fabric import Fabric
from enums.stuffed_animal_size import StuffedAnimalSize
from enums.stuffing import Stuffing
from exceptions.invalid_data_error import InvalidDataError


class ChristmasItemFactory(ItemFactory):
    """
    Concrete class for Christmas item factory
    """

    def create_toys(self, name, product_details, product_id):
        """
        Creates a Santa Workshop.
        :param name: name of the Santa's Workshop
        :param product_details: product details of the Santa's Workshop
        :param product_id: product id of the Santa's Workshop
        :return: Santa's Workshop
        """
        if product_details["has_batteries"] != "N":
            raise InvalidDataError("Santa's Workshop is not battery operated")
        return SantaWorkshop(
            name,
            product_details["description"],
            product_id,
            False,
            product_details["min_age"],
            tuple(map(int, product_details["dimensions"].split(","))),
            product_details["num_rooms"],
        )

    def create_stuffed_animal(self, name, product_details, product_id):
        """
        Creates a Reindeer.
        :param name: name of the Reindeer
        :param product_details: product details of the Reindeer
        :param product_id: product_id of the Reindeer
        :return: Reindeer
        """
        if product_details["fabric"] != Fabric.COTTON.value:
            raise InvalidDataError("Reindeer is always made out of cotton")
        if product_details["stuffing"] != Stuffing.WOOL.value:
            raise InvalidDataError("Reindeer is always stuffed with wool")
        if product_details["has_glow"] != "Y":
            raise InvalidDataError("Reindeer always has a glow")
        if product_details["size"] not in list(
            map(lambda s: s.value, StuffedAnimalSize)
        ):
            raise InvalidDataError(
                f"Size can only be one of {list(map(lambda s: s.value, StuffedAnimalSize))}"
            )
        return Reindeer(
            name,
            product_details["description"],
            product_id,
            Stuffing(product_details["stuffing"]),
            StuffedAnimalSize(product_details["size"]),
            Fabric(product_details["fabric"]),
            True,
        )

    def create_candy(self, name, product_details, product_id):
        """
        Creates a Candy Canes.
        :param name: name of the Candy Canes
        :param product_details: product details of the Candy Canes
        :param product_id: product_id of the Candy Canes
        :return: Candy Canes
        """
        if product_details["colour"] not in list(
            map(lambda c: c.value, CandyCaneColors)
        ):
            raise InvalidDataError(
                f"Color can only be one of {list(map(lambda c: c.value, CandyCaneColors))}"
            )
        if product_details["has_nuts"] != "N":
            raise InvalidDataError("Candy Canes cannot have nuts")
        if product_details["has_lactose"] != "N":
            raise InvalidDataError("Candy Canes cannot have lactose")
        return CandyCanes(
            name,
            product_details["description"],
            product_id,
            False,
            False,
            CandyCaneColors(product_details["colour"]),
        )
