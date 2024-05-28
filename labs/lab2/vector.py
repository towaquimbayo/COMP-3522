class Vector:
    def __init__(self, x, y, z):
        """
        Initialize a vector object.
        :param x: x coordinate
        :param y: y coordinate
        :param z: z coordinate
        :precondition: x, y, and z must be integers
        """
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        """
        Return the x coordinate of the vector.
        :return: x coordinate
        """
        return self._x

    def get_y(self):
        """
        Return the y coordinate of the vector.
        :return: y coordinate
        """
        return self._y

    def get_z(self):
        """
        Return the z coordinate of the vector.
        :return: z coordinate
        """
        return self._z

    def set_x(self, x):
        """
        Set the x coordinate of the vector.
        :param x: x coordinate
        """
        self._x = x

    def set_y(self, y):
        """
        Set the y coordinate of the vector.
        :param y: y coordinate
        """
        self._y = y

    def set_z(self, z):
        """
        Set the z coordinate of the vector.
        :param z: z coordinate
        """
        self._z = z

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    z = property(get_z, set_z)

    def add(self, vector):
        """
        Add a vector to the current vector.
        :param vector: vector to add to the current vector
        """
        self._x += vector.x
        self._y += vector.y
        self._z += vector.z

    def get_vector(self):
        """
        Return the vector.
        :return: vector as a tuple
        """
        return self._x, self._y, self._z

    def __str__(self):
        """
        Return the vector as a string.
        :return: vector as a string
        """
        return f"{self.x}, {self.y}, {self.z}"
