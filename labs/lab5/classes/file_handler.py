import json
from enums.file_extensions import FileExtension
from pathlib import Path
from exceptions.invalid_file_type_error import InvalidFileTypeError


class FileHandler:
    @staticmethod
    def convert_txt_to_dict(txt):
        try:
            result = {}
            for entry in txt.strip("{}").split(", "):
                parts = entry.split(": ")
                result[parts[0].strip('"')] = (
                    parts[1].strip('["]').split('", "') if len(parts) > 1 else [""]
                )
            return result
        except Exception as e:
            raise e

    @staticmethod
    def load_data(path, file_extension_enum):
        try:
            file_path = Path(path)
            if not file_path.exists():
                raise FileNotFoundError("File not found")
            if not file_path.is_file():
                raise TypeError("Path is not a file")
            if file_path.suffix[1:] not in [
                FileExtension.JSON.value,
                FileExtension.TXT.value,
            ]:
                raise InvalidFileTypeError(
                    "File extension is not supported. Choose a txt or json file."
                )
            if file_extension_enum.value != file_path.suffix[1:]:
                raise TypeError("File extension doesn't match.")
            with open(path, "r", encoding="utf-8") as file:
                return (
                    json.load(file)
                    if file_extension_enum.value == FileExtension.JSON.value
                    else FileHandler.convert_txt_to_dict(file.read())
                )
        except FileNotFoundError as e:
            raise e
        except InvalidFileTypeError as e:
            raise e
        except TypeError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def write_lines(path, lines):
        try:
            file_path = Path(path)
            if file_path.suffix[1:] not in [
                FileExtension.JSON.value,
                FileExtension.TXT.value,
            ]:
                raise InvalidFileTypeError(
                    "File extension is not supported. Choose a txt or json file."
                )
            with open(path, "a", encoding="utf-8") as file:
                file.writelines(lines)
        except InvalidFileTypeError as e:
            raise e
        except Exception as e:
            raise e
