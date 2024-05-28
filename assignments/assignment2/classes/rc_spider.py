from classes.toys import Toys


class RCSpider(Toys):
    def __init__(
        self,
        name,
        description,
        product_id,
        has_batteries,
        min_age,
        speed,
        jump_height,
        has_glow,
        type_of_spider,
    ):
        """
        Initializes the RC Spider.
        :param name: name of the RC Spider
        :param description: description of the RC Spider
        :param product_id: product id of the RC Spider
        :param has_batteries: True if the RC Spider is battery operated, False otherwise
        :param min_age: minimum age of the RC Spider
        :param speed: speed of the RC Spider
        :param jump_height: jump height of the RC Spider
        :param has_glow: True if the RC Spider has glow, False otherwise
        :param type_of_spider: type of the RC Spider
        """
        super().__init__(name, description, product_id, has_batteries, min_age)
        self.__speed = speed
        self.__jump_height = jump_height
        self.__has_glow = has_glow
        self.__type_of_spider = type_of_spider

    def get_speed(self):
        """
        Returns the speed of the RC Spider.
        :return: speed of the RC Spider
        """
        return self.__speed

    def set_speed(self, speed):
        """
        Sets the speed of the RC Spider.
        :param speed: speed of the RC Spider
        """
        self.__speed = speed

    def get_jump_height(self):
        """
        Returns the jump height of the RC Spider.
        :return: jump height of the RC Spider
        """
        return self.__jump_height

    def set_jump_height(self, jump_height):
        """
        Sets the jump height of the RC Spider.
        :param jump_height: jump height of the RC Spider
        """
        self.__jump_height = jump_height

    def get_has_glow(self):
        """
        Returns whether the RC Spider has glow.
        :return: True if the RC Spider has glow, False otherwise
        """
        return self.__has_glow

    def set_has_glow(self, has_glow):
        """
        Sets whether the RC Spider has glow.
        :param has_glow: True if the RC Spider has glow, False otherwise
        """
        self.__has_glow = has_glow

    def get_type_of_spider(self):
        """
        Returns the type of the RC Spider.
        :return: type of the RC Spider
        """
        return self.type_of_spider

    def set_type_of_spider(self, type_of_spider):
        """
        Sets the type of the RC Spider.
        :param type_of_spider: type of the RC Spider
        """
        self.type_of_spider = type_of_spider

    speed = property(get_speed, set_speed)
    jump_height = property(get_jump_height, set_jump_height)
    has_glow = property(get_has_glow, set_has_glow)
    type_of_spider = property(get_type_of_spider, set_type_of_spider)
