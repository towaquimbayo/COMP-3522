from item import Item

"""
This is the journal module. It contains the Journal class that represents a journal in a library.

@Author: Muhammad Noufil Saqib
@Version: 1.0.0
"""


class Journal(Item):
    def __init__(self, title, call_number, num_of_copies, author, issue_number, publisher):
        super().__init__(title, call_number, num_of_copies)
        self.author = author
        self.issue_number = issue_number
        self.publisher = publisher

    def __str__(self):
        """
        This function returns the string representation of the journal
        :return: the string representation of the journal
        """
        return (f"Title: {self.title}\nCall Number: {self.call_number}\nAuthor: {self.author}\n"
                f"Issue Number: {self.issue_number}\nPublisher: {self.publisher}\n"
                f"Available Copies: {self.num_of_copies}")
