from classes.item_factory import ItemFactory
from classes.robot_bunny import RobotBunny
from classes.easter_bunny import EasterBunny
from classes.creme_eggs import CremeEggs
from enums.fabric import Fabric
from enums.robot_bunny_colors import RobotBunnyColors
from enums.easter_bunny_colors import EasterBunnyColors
from enums.stuffed_animal_size import StuffedAnimalSize
from enums.stuffing import Stuffing
from exceptions.invalid_data_error import InvalidDataError


class EasterItemFactory(ItemFactory):
    """
    Concrete class for Easter item factory
    """

    def create_toys(self, name, product_details, product_id):
        """
        Creates a Robot Bunny.
        :param name: name of the Robot Bunny
        :param product_details: product details of the Robot Bunny
        :param product_id: product id of the Robot Bunny
        :return: Robot Bunny
        """
        if product_details["colour"] not in list(
            map(lambda c: c.value, RobotBunnyColors)
        ):
            raise InvalidDataError(
                f"Color can only be one of {list(map(lambda c: c.value, RobotBunnyColors))}"
            )
        if product_details["has_batteries"] != "Y":
            raise InvalidDataError("Robot Bunny is battery operated")
        return RobotBunny(
            name,
            product_details["description"],
            product_id,
            True,
            product_details["min_age"],
            product_details["num_sound"],
            RobotBunnyColors(product_details["colour"]),
        )

    def create_stuffed_animal(self, name, product_details, product_id):
        """
        Creates an Easter Bunny.
        :param name: name of the Easter Bunny
        :param product_details: product details of the Easter Bunny
        :param product_id: product_id of the Easter Bunny
        :return: Easter Bunny
        """
        if product_details["colour"] not in list(
            map(lambda c: c.value, EasterBunnyColors)
        ):
            raise InvalidDataError(
                f"Color can only be one of {list(map(lambda c: c.value, EasterBunnyColors))}"
            )
        if product_details["stuffing"] != Stuffing.POLYESTER_FIBREFILL.value:
            raise InvalidDataError(
                "Easter Bunny is always stuffed with polyester fiberfill"
            )
        if product_details["fabric"] != Fabric.LINEN.value:
            raise InvalidDataError("Easter Bunny is always made out of linen")
        if product_details["size"] not in list(
            map(lambda c: c.value, StuffedAnimalSize)
        ):
            raise InvalidDataError(
                f"Size can only be one of {list(map(lambda c: c.value, StuffedAnimalSize))}"
            )
        return EasterBunny(
            name,
            product_details["description"],
            product_id,
            Stuffing(product_details["stuffing"]),
            StuffedAnimalSize(product_details["size"]),
            Fabric(product_details["fabric"]),
            EasterBunnyColors(product_details["colour"]),
        )

    def create_candy(self, name, product_details, product_id):
        """
        Creates a Creme Eggs.
        :param name: name of the Creme Eggs
        :param product_details: product details of the Creme Eggs
        :param product_id: product_id of the Creme Eggs
        :return: Creme Eggs
        """
        if product_details["has_lactose"] != "Y":
            raise InvalidDataError("Creme Eggs always has lactose")
        return CremeEggs(
            name,
            product_details["description"],
            product_id,
            True if product_details["has_nuts"] == "Y" else False,
            True,
            product_details["pack_size"],
        )
