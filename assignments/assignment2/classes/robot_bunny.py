from classes.toys import Toys


class RobotBunny(Toys):
    def __init__(
        self, name, description, product_id, has_batteries, min_age, num_sound, color
    ):
        """
        Initializes the Robot Bunny.
        :param name: name of the Robot Bunny
        :param description: description of the Robot Bunny
        :param product_id: product id of the Robot Bunny
        :param has_batteries: True if the Robot Bunny has batteries, False otherwise
        :param min_age: minimum age of the Robot Bunny
        :param num_sound: number of sounds of the Robot Bunny
        :param color: color of the Robot Bunny
        """
        super().__init__(name, description, product_id, has_batteries, min_age)
        self.__num_sound = num_sound
        self.__color = color

    def get_num_sound(self):
        """
        Returns the number of sounds of the Robot Bunny.
        :return: number of sounds of the Robot Bunny
        """
        return self.__num_sound

    def set_num_sound(self, num_sound):
        """
        Sets the number of sounds of the Robot Bunny.
        :param num_sound: number of sounds of the Robot Bunny
        """
        self.__num_sound = num_sound

    def get_color(self):
        """
        Returns the color of the Robot Bunny.
        :return: color of the Robot Bunny
        """
        return self.__color

    def set_color(self, color):
        """
        Sets the color of the Robot Bunny.
        :param color: color of the Robot Bunny
        """
        self.__color = color

    num_sound = property(get_num_sound, set_num_sound)
    color = property(get_color, set_color)
