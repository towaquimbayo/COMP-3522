from classes.item_factory import ItemFactory
from classes.rc_spider import RCSpider
from enums.fabric import Fabric
from enums.stuffed_animal_size import StuffedAnimalSize
from enums.stuffing import Stuffing
from enums.type_of_spider import TypeOfSpider
from classes.dancing_skeleton import DancingSkeleton
from classes.pumpkin_caramel_toffee import PumpkinCaramelToffee
from enums.toffee_variety import ToffeeVariety
from exceptions.invalid_data_error import InvalidDataError


class HalloweenItemFactory(ItemFactory):
    """
    Concrete class for Halloween item factory
    """

    def create_toys(self, name, product_details, product_id):
        """
        Creates an RC Spider.
        :param name: name of the RC Spider
        :param product_details: product details of the RC Spider
        :param product_id: product id of the RC Spider
        :return: RC Spider
        """
        if product_details["spider_type"] not in list(
            map(lambda c: c.value, TypeOfSpider)
        ):
            raise InvalidDataError(
                f"Spider type can only be one of {list(map(lambda c: c.value, TypeOfSpider))}"
            )
        if product_details["has_batteries"] != "Y":
            raise InvalidDataError("RC Spider is battery operated")
        return RCSpider(
            name,
            product_details["description"],
            product_id,
            True,
            product_details["min_age"],
            product_details["speed"],
            product_details["jump_height"],
            True if product_details["has_glow"] == "Y" else False,
            TypeOfSpider(product_details["spider_type"]),
        )

    def create_stuffed_animal(self, name, product_details, product_id):
        """
        Creates a Dancing Skeleton.
        :param name: name of the Dancing Skeleton
        :param product_details: product details of the Dancing Skeleton
        :param product_id: product_id of the Dancing Skeleton
        :return: Dancing Skeleton
        """
        if product_details["stuffing"] != Stuffing.POLYESTER_FIBREFILL.value:
            raise InvalidDataError(
                "Dancing Skeleton is always stuffed with polyester fiberfill"
            )
        if product_details["fabric"] != Fabric.ACRYLIC.value:
            raise InvalidDataError("Dancing Skeleton is always made out of acrylic")
        if product_details["has_glow"] != "Y":
            raise InvalidDataError("Dancing Skeleton always has a glow")
        if product_details["size"] not in list(
            map(lambda c: c.value, StuffedAnimalSize)
        ):
            raise InvalidDataError(
                f"Size can only be one of {list(map(lambda c: c.value, StuffedAnimalSize))}"
            )
        return DancingSkeleton(
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
        Creates a Pumpkin Caramel Toffee.
        :param name: name of the Pumpkin Caramel Toffee
        :param product_details: product details of the Pumpkin Caramel Toffee
        :param product_id: product_id of the Pumpkin Caramel Toffee
        :return: Pumpkin Caramel Toffee
        """
        if product_details["variety"] not in list(
            map(lambda c: c.value, ToffeeVariety)
        ):
            raise InvalidDataError(
                f"Variety can only be one of {list(map(lambda c: c.value, ToffeeVariety))}"
            )
        if product_details["has_lactose"] != "Y":
            raise InvalidDataError("Pumpkin Caramel Toffee always has lactose")
        return PumpkinCaramelToffee(
            name,
            product_details["description"],
            product_id,
            True if product_details["has_nuts"] == "Y" else False,
            True,
            ToffeeVariety(product_details["variety"]),
        )
