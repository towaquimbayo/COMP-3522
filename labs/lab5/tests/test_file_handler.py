from unittest import TestCase
from classes.file_handler import FileHandler
from enums.file_extensions import FileExtension
from exceptions.invalid_file_type_error import InvalidFileTypeError


class TestFileHandler(TestCase):
    def test_convert_txt_to_dict(self):
        self.assertEqual(
            FileHandler.convert_txt_to_dict('{"key": ["value"]}'), {"key": ["value"]}
        )

    def test_load_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            FileHandler.load_data("../this_will_fail.json", FileExtension.JSON)

    def test_load_data_path_not_file(self):
        with self.assertRaises(TypeError):
            FileHandler.load_data("../", FileExtension.JSON)

    def test_load_data_invalid_file_type(self):
        with self.assertRaises(InvalidFileTypeError):
            FileHandler.load_data("../data.csv", FileExtension.JSON)

    def test_load_data_file_extension_mismatch(self):
        with self.assertRaises(TypeError):
            FileHandler.load_data("../data.json", FileExtension.TXT)

    def test_load_data_json(self):
        dictionary = FileHandler.load_data("../data.json", FileExtension.JSON)
        self.assertEqual(
            dictionary["hello"],
            ["Expression of greeting used by two or more people who meet each other."],
        )

    def test_load_data_txt(self):
        dictionary = FileHandler.load_data("../data.txt", FileExtension.TXT)
        self.assertEqual(
            dictionary["hello"],
            ["Expression of greeting used by two or more people who meet each other."],
        )

    def test_write_lines_invalid_file_type(self):
        with self.assertRaises(InvalidFileTypeError):
            FileHandler.write_lines("output.csv", "test")

    def test_write_lines(self):
        FileHandler.write_lines("output.txt", "test")
        with open("output.txt", "r") as file:
            self.assertEqual(file.read(), "test")

    def test_write_lines_append(self):
        FileHandler.write_lines("output.txt", "test")
        FileHandler.write_lines("output.txt", "test")
        with open("output.txt", "r") as file:
            self.assertEqual(file.read(), "testtest")

    def tearDown(self):
        with open("output.txt", "w") as file:
            file.write("")
