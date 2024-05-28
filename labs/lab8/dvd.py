from item import Item

"""
This is the dvd module. It contains the DVD class that represents a DVD in a library.

@Author: Muhammad Noufil Saqib
@Version: 1.0.0
"""


class DVD(Item):
    def __init__(self, title, call_number, num_of_copies, release_date, region_code):
        super().__init__(title, call_number, num_of_copies)
        self.release_date = release_date
        self.region_code = region_code

    def __str__(self):
        """
        This function returns the string representation of the DVD
        :return: the string representation of the DVD
        """
        return (f"Title: {self.title}\nCall Number: {self.call_number}\nRelease Date: {self.release_date}\n"
                f"Region Code: {self.region_code}\nAvailable Copies: {self.num_of_copies}")
