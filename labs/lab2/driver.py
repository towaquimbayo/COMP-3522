from asteroid import Asteroid
from vector import Vector
from random import randint
from datetime import datetime
import time
import math


class Controller:
    def __init__(self):
        """
        Initialize a controller object.
        This controller object will be used to simulate the movement of asteroids.
        Creates a list of asteroids
        """
        self._asteroids = []
        self.__add_asteroid()

    def __add_asteroid(self):
        """
        Add 100 asteroids to the list of asteroids.
        Radius is between 1 and 4 metres.
        Position is between (0, 0, 0) and (100, 100, 100).
        Velocity is between (-5, -5, -5) and (5, 5, 5).
        """
        for i in range(100):
            radius = randint(1, 4)
            position = Vector(randint(0, 100), randint(0, 100), randint(0, 100))
            velocity = Vector(randint(-5, 5), randint(-5, 5), randint(-5, 5))
            self._asteroids.append(Asteroid(radius * math.pi * 2, position, velocity))

    def simulate(self, seconds):
        """
        Simulate the movement of asteroids for a given number of seconds.
        The simulation will start at the beginning of the next precise second.
        Each asteroid will move once per second for the given number of seconds and print its new position.
        :param seconds: number of seconds to simulate
        :precondition: seconds must be an integer
        """
        wait_time = 1 - int(datetime.now().microsecond / 100000.0) / 10
        if wait_time != 1:
            time.sleep(wait_time)
        start = datetime.now()
        print("Simulation Start Time:", start, "\n\nMoving Asteroids!\n-----------------")
        for i in range(seconds):
            time.sleep(1 - (datetime.now() - start).total_seconds() % 1)
            for asteroid in self._asteroids:
                old_position = Vector(asteroid.get_position().x, asteroid.get_position().y, asteroid.get_position().z)
                new_position = asteroid.move()
                print(f"Asteroid {asteroid.uid} Moved! Old Pos: {old_position} -> New Pos: {new_position}\n{asteroid}")


def main():
    controller = Controller()
    controller.simulate(10)


if __name__ == "__main__":
    main()
