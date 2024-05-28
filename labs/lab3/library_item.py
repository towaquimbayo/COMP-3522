import abc


class LibraryItem(abc.ABC):
    def __init__(self, title, call_number, num_of_copies):
        self.title = title
        self.call_number = call_number
        self.num_of_copies = num_of_copies

    def check_availability(self):
        return self.num_of_copies > 0

    def get_item_instance(self):
        return type(self).__name__

    @abc.abstractmethod
    def __str__(self):
        pass
