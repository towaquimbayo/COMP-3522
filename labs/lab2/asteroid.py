from vector import Vector


class Asteroid:
    _id = 1

    def __init__(self, circumference, position, velocity):
        """
        Initialize an asteroid object.
        :param circumference: circumference of the asteroid in metres
        :param position: position of the asteroid as a Vector object
        :param velocity: velocity of the asteroid as a Vector object
        :precondition: radius must be an integer
        :precondition: position must be a Vector object
        :precondition: velocity must be a Vector object
        """
        self._uid = self._id
        self._circumference = circumference
        self._position = Vector(position.x, position.y, position.z)
        self._velocity = Vector(velocity.x, velocity.y, velocity.z)
        self._increment_id()

    @classmethod
    def _increment_id(cls):
        """
        Increment the id of the asteroid. Invoked when an asteroid is created.
        """
        cls._id += 1

    def get_id(self):
        """
        Return the id of the asteroid.
        :return: id of the asteroid
        """
        return self._uid

    def get_circumference(self):
        """
        Return the circumference of the asteroid.
        :return: circumference of the asteroid
        """
        return self._circumference

    def get_position(self):
        """
        Return the position of the asteroid.
        :return: position of the asteroid as a Vector object
        """
        return self._position

    def get_velocity(self):
        """
        Return the velocity of the asteroid.
        :return: velocity of the asteroid as a Vector object
        """
        return self._velocity

    def set_id(self, uid):
        """
        Set the id of the asteroid.
        :param uid: id of the asteroid
        """
        self._uid = uid

    def set_circumference(self, circumference):
        """
        Set the circumference of the asteroid.
        :param circumference: circumference of the asteroid
        """
        self._circumference = circumference

    def set_position(self, position):
        """
        Set the position of the asteroid.
        :param position: position of the asteroid as a Vector object
        """
        self._position = position

    def set_velocity(self, velocity):
        """
        Set the velocity of the asteroid.
        :param velocity: velocity of the asteroid as a Vector object
        """
        self._velocity = velocity

    uid = property(get_id, set_id)
    circumference = property(get_circumference, set_circumference)
    position = property(get_position, set_position)
    velocity = property(get_velocity, set_velocity)

    def move(self):
        """
        Move the asteroid by adding its velocity to its position.
        :return: new position of the asteroid as a Vector object
        """
        self.position.add(self.velocity)
        return self.position

    def __str__(self):
        """
        Return a string that describes the asteroid.
        :return: string that describes the asteroid
        """
        return (f"Asteroid {self._uid} is currently at {self.position} and moving at {self.velocity} metres per second."
                f" It has a circumference of {self._circumference}")
