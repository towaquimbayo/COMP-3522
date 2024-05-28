import math


def calculate_hypotenuse(side_a, side_b):
    """
    Calculates the hypotenuse of a right triangle
    :param side_a: length of one side of the triangle
    :param side_b: length of the other side of the triangle
    :precondition: side_a and side_b must be positive integers
    :return: hypotenuse of a right triangle
    """
    return math.sqrt(side_a**2 + side_b**2)
