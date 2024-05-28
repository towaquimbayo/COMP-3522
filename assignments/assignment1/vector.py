class Vector:
    def __init__(self, x, y):
        """
        Initializes a Vector object with x and y coordinates.
        :param x: int representing the x coordinate
        :param y: int representing the y coordinate
        """
        self.__x = x
        self.__y = y

    def get_x(self):
        """
        Gets the x coordinate.
        :return: int representing the x coordinate
        """
        return self.__x

    def get_y(self):
        """
        Gets the y coordinate.
        :return: int representing the y coordinate
        """
        return self.__y

    def set_x(self, x):
        """
        Sets the x coordinate.
        :param x: int representing the x coordinate
        """
        self.__x = x

    def set_y(self, y):
        """
        Sets the y coordinate.
        :param y: int representing the y coordinate
        """
        self.__y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)

    def __eq__(self, other):
        """
        Checks if the x and y coordinates of the vector are equal to the x and y coordinates of another vector.
        :param other: Vector object representing the other vector to compare with
        :return: True if the x and y coordinates are equal, False otherwise
        """
        return self.__x == other.x and self.__y == other.y

    def __str__(self):
        """
        Returns a string representation of the vector.
        :return: string representation of the vector
        """
        return f"X coordinate at {self.x}, Y coordinate at {self.y}"
