from book import Book
from dvd import Dvd
from journal import Journal


class LibraryItemGenerator:
    @staticmethod
    def generate_item():
        try:
            option = input("Choose an item to add:\n1. Book\n2. DVD\n3. Journal\nEntered option number: ")
            if int(option) == 1:
                return Book(input("Enter title: "), input("Enter call number: "), input("Enter number of copies: "),
                            input("Enter author: "))
            elif int(option) == 2:
                return Dvd(input("Enter title: "), input("Enter call number: "), input("Enter number of copies: "),
                           input("Enter release date: "), input("Enter region code: "))
            elif int(option) == 3:
                return Journal(input("Enter title: "), input("Enter call number: "), input("Enter number of copies: "),
                               input("Enter issue number: "), input("Enter publisher: "))
            else:
                print("Invalid input. Failed to add item.\n")
                return None
        except ValueError:
            print("Invalid input. Failed to add item.\n")
            return None
