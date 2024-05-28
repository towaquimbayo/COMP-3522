import pygame
from vector import Vector
from drawable import Drawable


class Block(Drawable):
    def __init__(self, screen, position, block_size, color, border_width=0):
        """
        Initializes a Block object that represents a single block on the screen.
        :param screen: pygame.Surface object representing the screen
        :param position: Vector object representing the position of the block
        :param block_size: int representing the size of the block
        :param color: tuple representing the color of the block
        :param border_width: int representing the width of the border of the block
        """
        self.__screen = screen
        self.__position = Vector(position.x, position.y)
        self.__block_size = block_size
        self.__color = color
        self.__border_width = border_width

    def get_position(self):
        """
        Gets the position of the block.
        :return: Vector object representing the position of the block
        """
        return self.__position

    def set_position(self, position):
        """
        Sets the position of the block.
        :param position: Vector object representing the position of the block
        """
        self.__position = Vector(position.x, position.y)

    position = property(get_position, set_position)

    def position_equals(self, other):
        """
        Checks if the position of the block is equal to the position
        of another block by comparing their x and y values.
        :param other: Block object representing the other block to compare with
        :return: True if the positions are equal, False otherwise
        """
        return self.position.__eq__(other.position)

    def draw(self):
        """
        Draws the block on the screen.
        """
        pygame.draw.rect(
            self.__screen,
            self.__color,
            pygame.Rect(
                self.__position.x,
                self.__position.y,
                self.__block_size,
                self.__block_size,
            ),
            self.__border_width,
        )
