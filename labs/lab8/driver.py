from book import Book
from dvd import DVD
from journal import Journal
from library import Library

"""
This is the driver module. It contains the main function that creates a library.

@Author: Muhammad Noufil Saqib
@Version: 1.0.0
"""


def main():
    # Creating items
    items = [
        Book("The Catcher in the Rye", "C123", "J.D. Salinger", 3),
        Book("To Kill a Mockingbird", "M456", "Harper Lee", 5),
        DVD("The Godfather", "D789", 2, "1972", 1),
        DVD("The Shawshank Redemption", "S147", 9, "1994", 2),
        Journal("Journal of Econometrics", "J159", 1, "James Heckman", "4", "Elsevier"),
        Journal("Journal of Finance", "J951", 2, "Eugene Fama", "2", "Wiley")
    ]

    my_library = Library(items)

    # Adding items to the library
    my_library.add_item()

    # Display available books
    my_library.display_available_items()

    # Find books by title
    found_books = my_library.find_items("Mockingbird")
    if found_books:
        print("\nBooks found:")
        for found_book in found_books:
            print(found_book)

    # Check out a book
    my_library.check_out("C123")
    my_library.display_available_items()

    # Return a book
    my_library.return_item("C123")
    my_library.display_available_items()

    # Remove a book
    my_library.remove_item("M456")
    my_library.display_available_items()


if __name__ == "__main__":
    main()
