class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words_dict = collections.defaultdict(list)
        self.word_set = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words_dict[len(word)].append(word)
        self.word_set.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if '.' not in word:
            return word in self.word_set

        for v in self.words_dict[len(word)]:
            for i, c in enumerate(word):
                if c != v[i] and c != '.': break
            else:
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
