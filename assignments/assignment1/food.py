from entity import Entity
from block import Block
from vector import Vector
from random import randint
from drawable import Drawable


class Food(Entity, Drawable):
    def __init__(self, screen):
        """
        Initializes a Food object with a random position on the screen.
        :param screen: pygame screen object
        """
        super().__init__(screen)
        columns = self.screen.get_width() // self.block_size - 2
        rows = self.screen.get_height() // self.block_size - 2
        # setting x position range from 3 because the Snake size is 120 (3 blocks * 40px)
        self.__block = Block(
            self.screen,
            Vector(
                randint(3, columns) * self.block_size,
                randint(1, rows) * self.block_size,
            ),
            self.block_size,
            (255, 0, 0),
        )
        self.__snake_positions = []

    def get_position(self):
        """
        Returns the position of the food.
        :return: Vector object representing the position of the food
        """
        return self.__block.position

    def set_position(self, position):
        """
        Sets the position of the food.
        :param position: Vector object representing the position of the food
        """
        self.__block.position = position

    def get_block(self):
        """
        Returns the Block object representing the food.
        :return: Block object representing the food
        """
        return self.__block

    position = property(get_position, set_position)

    def draw(self):
        """
        Draws the food on the screen.
        """
        self.__block.draw()

    def set_snake_position(self, snake_positions):
        """
        Sets the snake's position to a list of Vector objects.
        :param snake_positions: list of Vector objects representing the snake's positions
        :precondition: snake_positions must be a list of Vector objects
        """
        self.__snake_positions = snake_positions

    def collided(self):
        """
        Resets the position of the food to a new random position on the screen.
        Also, the food should not be placed on top of the snake's body.
        """
        while True:
            new_position = Vector(
                randint(1, self.screen.get_width() // self.block_size - 2)
                * self.block_size,
                randint(1, self.screen.get_height() // self.block_size - 2)
                * self.block_size,
            )

            # Check if new position is not in the snake's body
            if new_position not in self.__snake_positions:
                self.__block.position = new_position
                break

    def __str__(self):
        """
        Returns a string representation of the food.
        :return: string representation of the food
        """
        return f"The food's positioned at {self.position.x}, {self.position.y} and has a size of {self.block_size}"
