from library import Library


def main():
    my_library = Library()
    my_library.add_item()
    # my_library.add_item()
    # my_library.add_item()

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
