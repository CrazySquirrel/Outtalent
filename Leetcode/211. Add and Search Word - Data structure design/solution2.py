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
        l = len(word)

        def dfs(node: Node, i: int):
            if i == l: return node.isword

            c = word[i]

            if c == '.':
                if node.children:
                    for child in node.children.values():
                        if dfs(child, i + 1): return True
                    return False
                else:
                    return False
            else:
                if c in node.children:
                    return dfs(node.children[c], i + 1)
                else:
                    return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
