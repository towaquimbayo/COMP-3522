import abc


class Entity(abc.ABC):
    def __init__(self, screen):
        """
        Initializes an Entity object that represents an entity on the screen.
        :param screen: pygame.Surface object representing the screen
        """
        self.__screen = screen
        self.__block_size = 40

    def get_screen(self):
        """
        Gets the screen.
        :return: pygame.Surface object representing the screen
        """
        return self.__screen

    def set_screen(self, screen):
        """
        Sets the screen.
        :param screen: pygame.Surface object representing the screen
        """
        self.__screen = screen

    def get_block_size(self):
        """
        Gets the block size.
        :return: int representing the block size
        """
        return self.__block_size

    def set_block_size(self, size):
        """
        Sets the block size.
        :param size: int representing the block size
        """
        self.__block_size = size

    screen = property(get_screen, set_screen)
    block_size = property(get_block_size, set_block_size)

    @abc.abstractmethod
    def collided(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
