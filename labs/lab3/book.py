from library_item import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, call_number, num_of_copies, author):
        super().__init__(title, call_number, num_of_copies)
        self.author = author

    def __str__(self):
        return (f"Title: {self.title}\nCall Number: {self.call_number}\n"
                f"Author: {self.author}\nAvailable Copies: {self.num_of_copies}")
