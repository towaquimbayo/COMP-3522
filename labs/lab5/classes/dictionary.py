from classes.file_handler import FileHandler
from enums.file_extensions import FileExtension
from pathlib import Path
import difflib as dl


class Dictionary:
    def __init__(self):
        self.data = {}

    def load_dictionary(self, filepath):
        loaded_data = FileHandler.load_data(
            filepath,
            FileExtension.JSON
            if Path(filepath).suffix[1:] == FileExtension.JSON.value
            else FileExtension.TXT,
        )
        self.data = {
            word.lower(): definition for word, definition in loaded_data.items()
        }

    def query_definition(self, word):
        word = word.lower()
        definition = self.data.get(word, "Word not found.")
        FileHandler.write_lines("output.txt", f"{word}: {definition}\n")
        if not self.data:
            return "Dictionary is empty. Please load a dictionary first."
        if definition == "Word not found.":
            similar_words = dl.get_close_matches(word, self.data.keys())
            if similar_words:
                return (
                    f"No exact matches found. Did you mean: {', '.join(similar_words)}?"
                )
            return definition
        return " ".join(definition)  # removes the brackets from the output
