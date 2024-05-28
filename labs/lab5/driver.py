# Name: Towa Quimbayo
# Student number: A01086002
from classes.dictionary import Dictionary


def main():
    try:
        dictionary = Dictionary()
        dictionary.load_dictionary("data.json")
        while True:
            word = input("Enter a word: ")
            if word == "exitprogram":
                break
            print(f"Definition: {dictionary.query_definition(word)}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
