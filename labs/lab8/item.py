import abc

"""
This is an abstract class that represents an item in a library.
    
@Author: Muhammad Noufil Saqib
@Version: 1.0.0
"""


class Item(abc.ABC):
    def __init__(self, title, call_number, num_of_copies):
        self.title = title
        self.call_number = call_number
        self.num_of_copies = num_of_copies

    def add_copy(self):
        """
        This function increases the number of copies of the item
        :return: None
        """
        self.num_of_copies += 1

    def remove_copy(self):
        """
        This function decreases the number of copies of the item
        :return: None
        """
        self.num_of_copies -= 1

    def check_availability(self):
        """
        This function checks if the item is available
        :return: True if the item is available, False otherwise
        """
        return self.num_of_copies > 0

    @abc.abstractmethod
    def __str__(self):
        """
        This abstract method returns the string representation of the item
        :return: the string representation of the item
        """
        pass
