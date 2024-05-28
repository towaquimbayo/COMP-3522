from book_item_factory import BookItemFactory
from dvd_item_factory import DVDItemFactory
from journal_item_factory import JournalItemFactory

"""
This is the library item generator module. It contains the generate function that generates a library item.

@Author: Muhammad Noufil Saqib
@Version: 1.0.0
"""


class LibraryItemGenerator:
    @staticmethod
    def generate():
        """
        This function generates a library item
        :return: the generated library item
        """
        print("Enter the type of item to add: ")
        print("1. Book")
        print("2. DVD")
        print("3. Journal")
        choice = input("Enter choice (1-3): ")

        title = input("Enter the title: ")
        call_number = input("Enter the call number: ")
        num_of_copies = int(input("Enter the number of copies: "))

        if choice == "1":
            factory = BookItemFactory()
            author = input("Enter the author: ")

            return factory.create_item(title=title, call_number=call_number, num_of_copies=num_of_copies, author=author)
        elif choice == "2":
            factory = DVDItemFactory()
            release_date = input("Enter the release date: ")
            region_code = input("Enter the region code: ")

            return factory.create_item(title=title, call_number=call_number, num_of_copies=num_of_copies,
                                       release_date=release_date, region_code=region_code)
        elif choice == "3":
            factory = JournalItemFactory()
            author = input("Enter the author: ")
            issue_number = input("Enter the issue number: ")
            publisher = input("Enter the publisher: ")

            return factory.create_item(title=title, call_number=call_number, num_of_copies=num_of_copies,
                                       author=author, issue_number=issue_number, publisher=publisher)
        else:
            print("Invalid choice")
        return
