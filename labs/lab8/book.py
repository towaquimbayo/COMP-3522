from item import Item

"""
This is the book module. It contains the Book class that represents a book in a library.

@Author: Muhammad Noufil Saqib
@Version: 1.0.0
"""


class Book(Item):
    def __init__(self, title, call_number, author, num_of_copies):
        super().__init__(title, call_number, num_of_copies)
        self.author = author

    def __str__(self):
        """
        This function returns the string representation of the book
        :return: the string representation of the book
        """
        return (f"Title: {self.title}\nCall Number: {self.call_number}\nAuthor: {self.author}\n"
                f"Available Copies: {self.num_of_copies}")
