from library_item import LibraryItem


class Dvd(LibraryItem):
    def __init__(self, title, call_number, num_of_copies, release_date, region_code):
        super().__init__(title, call_number, num_of_copies)
        self.release_date = release_date
        self.region_code = region_code

    def __str__(self):
        return (f"Title: {self.title}\nCall Number: {self.call_number}\n"
                f"Release date: {self.release_date}\nRegion code: {self.region_code}\n"
                f"Available Copies: {self.num_of_copies}")
