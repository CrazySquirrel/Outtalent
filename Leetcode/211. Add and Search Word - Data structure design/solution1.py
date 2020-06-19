class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for w in word: current = current.children[w]
        current.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def dfs(node: Node, i: int):
            if node is None: return False
            if i == len(word): return node.isword

            if word[i] == '.':
                return any([dfs(child, i + 1) for child in node.children.values()] if node.children else [False])
            else:
                return dfs(node.children.get(word[i]), i + 1)

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
