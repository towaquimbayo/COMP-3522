from classes.stuffed_animal import StuffedAnimal


class DancingSkeleton(StuffedAnimal):
    def __init__(self, name, description, product_id, stuffing, size, fabric, has_glow):
        """
        Initializes the dancing skeleton.
        :param name: name of the dancing skeleton
        :param description: description of the dancing skeleton
        :param product_id: product id of the dancing skeleton
        :param stuffing: stuffing of the dancing skeleton
        :param size: size of the dancing skeleton
        :param fabric: fabric of the dancing skeleton
        :param has_glow: True if the dancing skeleton has a glow, False otherwise
        """
        super().__init__(
            name,
            description,
            product_id,
            stuffing,
            size,
            fabric,
        )
        self.__has_glow = has_glow

    def get_has_glow(self):
        """
        Returns whether the dancing skeleton has a glow.
        :return: True if the dancing skeleton has a glow, False otherwise
        """
        return self.__has_glow

    def set_has_glow(self, has_glow):
        """
        Sets whether the dancing skeleton has a glow.
        :param has_glow: True if the dancing skeleton has a glow, False otherwise
        """
        self.__has_glow = has_glow

    has_glow = property(get_has_glow, set_has_glow)
