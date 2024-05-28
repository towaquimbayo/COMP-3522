"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation. Redefined as a string for optimization.
    COMMON_PUNCTUATION = ",*;.:()[]"

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # created a punctuation table that will be used to remove punctuation from words.
        punc_table = str.maketrans('', '', self.COMMON_PUNCTUATION)
        words_list = []
        with open(src, mode='r', encoding='utf-8') as book_file:
            for line in book_file:
                if line != "\n":
                    words = line.split()
                    # remove common punctuation from words and add them to the list of words.
                    words_list.extend([word.translate(punc_table) for word in words])
        self.text = words_list

    def find_unique_words(self):
        """
        Filters out all the words in the text.
        Uses a set to filter out the words since Sets only contain unique values and
        comprehensions are faster than loops. Having to check for lowercase words prevents
        from double counting words that are the same but have different cases.
        :return: a set of all the unique words.
        """
        return set([word.lower() for word in self.text])


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    for word in unique_words:
        print(word)
    print("-" * 50)


if __name__ == '__main__':
    main()
