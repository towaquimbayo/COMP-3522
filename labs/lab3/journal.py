from library_item import LibraryItem


class Journal(LibraryItem):
    def __init__(self, title, call_number, num_of_copies, issue_number, publisher):
        super().__init__(title, call_number, num_of_copies)
        self.issue_number = issue_number
        self.publisher = publisher

    def __str__(self):
        return (f"Title: {self.title}\nCall Number: {self.call_number}\n"
                f"Issue number: {self.issue_number}\nPublisher: {self.publisher}\n"
                f"Available Copies: {self.num_of_copies}")
