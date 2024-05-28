import pygame

from entity import Entity
from block import Block
from vector import Vector
from direction import Direction
from drawable import Drawable


class Snake(Entity, Drawable):
    def __init__(self, screen):
        """
        Initializes a Snake object with a list of Block objects that represent the snake's body.
        Initial direction is right.
        :param screen: pygame screen object
        """
        super().__init__(screen)
        self.__previous_direction = Direction.RIGHT
        self.__direction = Direction.RIGHT
        self.__segments = self.__load_segments()
        self.__auto_pilot = False
        self.__final_path = []
        self.__visited = []

    def get_direction(self):
        """
        Returns the direction of the snake's head.
        :return: Direction enum
        """
        return self.__direction

    def set_direction(self, direction):
        """
        Sets the direction of the snake's head.
        :param direction: Direction enum
        :precondition: direction must be a Direction enum
        and cannot be the opposite direction of the snake's current direction
        """
        opposite_direction = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }
        # Check if the snake's head is moving in the opposite direction
        if direction != opposite_direction.get(self.__direction):
            self.__direction = direction
        self.__previous_direction = direction

    def get_auto_pilot(self):
        """
        Returns the autopilot mode of the snake.
        :return: boolean value
        """
        return self.__auto_pilot

    def set_auto_pilot(self, auto_pilot):
        """
        Sets the autopilot mode of the snake.
        :param auto_pilot: boolean value
        :precondition: auto_pilot must be a boolean value
        """
        self.__auto_pilot = auto_pilot

    direction = property(get_direction, set_direction)
    auto_pilot = property(get_auto_pilot, set_auto_pilot)

    def __load_segments(self):
        """
        Returns a list of Block objects that represent the snake's body.
        Initial snake size is 3 blocks.
        :return: list of Block objects
        """
        segments = []
        for i in range(0, 3):
            segments.append(
                Block(
                    self.screen,
                    Vector(i * self.block_size, 0),
                    self.block_size,
                    (0, 255, 0),
                )
            )
        return segments

    def get_positions(self):
        """
        Returns a list of Vector objects that represent the position of each block in the snake's body.
        :return: list of Vector objects representing the position of each block in the snake's body
        """
        return [segment.position for segment in self.__segments]

    def draw(self):
        """
        Draws the snake's segments on the screen.
        """
        if self.__auto_pilot:
            # draw the visited nodes
            for vector in self.__visited:
                pygame.draw.rect(
                    self.screen,
                    (66, 135, 245),
                    (
                        vector.x,
                        vector.y,
                        self.block_size,
                        self.block_size,
                    ),
                )

            # draw the final path
            for vector in self.__final_path:
                pygame.draw.rect(
                    self.screen,
                    (252, 186, 3),
                    (
                        vector.x,
                        vector.y,
                        self.block_size,
                        self.block_size,
                    ),
                    2,
                )

        # draw the snake
        for block in self.__segments:
            block.draw()

    def move(self, food):
        """
        Moves the snake's body by one block in the direction of the snake's head and updates the position of each
        block in the snake's body. The snake's body is always moving in the direction of the snake's head.
        """
        new_position = {
            Direction.UP: (0, -self.block_size),
            Direction.DOWN: (0, self.block_size),
            Direction.LEFT: (-self.block_size, 0),
            Direction.RIGHT: (self.block_size, 0),
        }

        head = self.__segments[-1]

        for i in range(len(self.__segments) - 1):
            self.__segments[i].position = self.__segments[i + 1].position

        def find_neighbours(segment_pos):
            """
            Finds the neighbours of the snake's head. Neighbours are the positions that the snake's head can move to.
            We set the neighbours' positions in a list comprehension
            and filter out the positions that are outside the screen boundaries.
            :param segment_pos: Vector object representing the position of the snake's head
            :return: filtered list of Vector objects representing the neighbours of the snake's head
            """
            neighbors = [
                Vector(segment_pos.x + self.block_size, segment_pos.y),
                Vector(segment_pos.x - self.block_size, segment_pos.y),
                Vector(segment_pos.x, segment_pos.y + self.block_size),
                Vector(segment_pos.x, segment_pos.y - self.block_size),
            ]
            return [
                n
                for n in neighbors
                if 0 <= n.x < self.screen.get_width()
                and 0 <= n.y < self.screen.get_height()
            ]

        def find_path():
            """
            Finds the shortest path from the snake's head to the food.
            :return: list of Vector objects representing the shortest path from the snake's head to the food
            """
            visited = []
            queue = [(head.position, [head.position])]

            while queue:
                snake_segment, path_route = queue.pop(0)
                if snake_segment == food.get_block().position:
                    self.__final_path = path_route
                    self.__visited = visited
                    return path_route
                neighbours = find_neighbours(snake_segment)
                # filter out the neighbours that are already visited or are in the snake's body
                # by using list comprehension
                valid_neighbours = [
                    n
                    for n in neighbours
                    if n not in visited and n not in self.get_positions()
                ]
                for neighbour in valid_neighbours:
                    visited.append(neighbour)
                    queue.append((neighbour, path_route + [neighbour]))
            return None

        if self.__auto_pilot:
            paths = find_path()
            if paths is not None and len(paths) > 1:
                if paths[1].x > paths[0].x:
                    self.direction = Direction.RIGHT
                elif paths[1].x < paths[0].x:
                    self.direction = Direction.LEFT
                elif paths[1].y > paths[0].y:
                    self.direction = Direction.DOWN
                elif paths[1].y < paths[0].y:
                    self.direction = Direction.UP

        # Update the position of the snake's head
        head.position.x += new_position.get(self.direction)[0]
        head.position.y += new_position.get(self.direction)[1]

        # Check if Snake hit the wall
        if self.__collided_with_wall():
            raise Exception("Snake hit the wall")
        if self.__collided_with_itself():
            raise Exception("Snake hit itself")

    def is_collided(self, food):
        """
        Checks if the snake's head has collided with the food.
        :param food: Food object
        :return: True if collided, False otherwise
        """
        return self.__segments[-1].position_equals(food)

    def collided(self):
        """
        Adds a new block to the snake's body when the snake's head collides with the food.
        The new block is added to the snake's body in the direction of the snake's head.
        """
        head = self.__segments[-1]
        new_block_position = {
            Direction.UP: Vector(
                head.position.x,
                head.position.y - self.block_size,
            ),
            Direction.DOWN: Vector(
                head.position.x,
                head.position.y + self.block_size,
            ),
            Direction.LEFT: Vector(
                head.position.x - self.block_size,
                head.position.y,
            ),
            Direction.RIGHT: Vector(
                head.position.x + self.block_size,
                head.position.y,
            ),
        }
        self.__increase_snake_size(new_block_position[self.direction])

    def __increase_snake_size(self, position):
        """
        Increases the size of the snake by appending a new block to the snake's body.
        :param position: Vector object representing the position of the new block
        """
        self.__segments.append(
            Block(
                self.screen,
                position,
                self.block_size,
                (0, 255, 0),
            )
        )

    def __collided_with_wall(self):
        """
        Checks if the snake's head has collided with the wall.
        :return: True if collided, False otherwise
        """
        head = self.__segments[-1]
        return (
            head.position.x < 0
            or head.position.x > self.screen.get_width() - self.block_size
            or head.position.y < 0
            or head.position.y > self.screen.get_height() - self.block_size
        )

    def __collided_with_itself(self):
        """
        Checks if the snake's head has collided with itself.
        :return: True if collided, False otherwise
        """
        head = self.__segments[-1]
        return any(head.position_equals(body) for body in self.__segments[:-1])

    def __str__(self):
        """
        Returns a string representation of the snake.
        :return: string representation of the snake
        """
        return (
            f"The snake's head positioned at {self.__segments[-1].position.x}, {self.__segments[-1].position.y} "
            f"and has a size of {self.block_size * len(self.__segments)}"
        )
