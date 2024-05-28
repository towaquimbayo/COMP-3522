from unittest import TestCase
from classes.dictionary import Dictionary


class TestDictionary(TestCase):
    def setUp(self):
        self.dictionary = Dictionary()

    def test_load_dictionary_json(self):
        self.dictionary.load_dictionary("../data.json")
        self.assertNotEquals(len(self.dictionary.data), 0)

    def test_load_dictionary_txt(self):
        self.dictionary.load_dictionary("../data.txt")
        self.assertNotEquals(len(self.dictionary.data), 0)

    def test_load_dictionary_lowercase_keys(self):
        self.dictionary.load_dictionary("../data.json")
        self.assertTrue(
            all(key.islower() for key in self.dictionary.data.keys() if key.isalpha())
        )

    def test_query_definition_empty_dictionary(self):
        self.assertEqual(
            self.dictionary.query_definition("test"),
            "Dictionary is empty. Please load a dictionary first.",
        )

    def test_query_definition_word_not_found(self):
        self.dictionary.load_dictionary("../data.json")
        self.assertEqual(self.dictionary.query_definition("xzx"), "Word not found.")

    def tearDown(self):
        with open("output.txt", "w") as file:
            file.write("")

    def test_query_definition_saves_queried_words(self):
        self.dictionary.load_dictionary("../data.json")
        self.dictionary.query_definition("hello")
        with open("output.txt", "r") as file:
            self.assertEqual(
                file.read(),
                "hello: ['Expression of greeting used by two or more people who meet each other.']\n",
            )

    def test_query_definition_word_found(self):
        self.dictionary.load_dictionary("../data.json")
        self.assertEqual(
            self.dictionary.query_definition("hello"),
            "Expression of greeting used by two or more people who meet each other.",
        )

    def test_query_definition_word_case_insensitive(self):
        self.dictionary.load_dictionary("../data.json")
        self.assertEqual(
            self.dictionary.query_definition("HeLlO"),
            "Expression of greeting used by two or more people who meet each other.",
        )

    def test_query_definition_similar_words(self):
        self.dictionary.load_dictionary("../data.json")
        self.assertEqual(
            self.dictionary.query_definition("bcit"),
            "No exact matches found. Did you mean: bit, obit, clit?",
        )
