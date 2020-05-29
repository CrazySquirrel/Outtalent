class TrieNode:
    def __init__(self):
        self.links = {}
        self.end = False

    def contains_key(self, c: str) -> bool:
        return c in self.links

    def get_links(self):
        return len(self.links)

    def get(self, c: str) -> "TrieNode":
        return self.links[c]

    def put(self, c: str, node: "TrieNode"):
        self.links[c] = node

    def set_end(self):
        self.end = True

    def is_end(self) -> bool:
        return self.end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root

        for i in range(len(word)):
            if not node.contains_key(word[i]):
                node.put(word[i], TrieNode())

            node = node.get(word[i])

        node.set_end()

    def search_prefix(self, word: str) -> "TrieNode":
        node = self.root

        for i in range(len(word)):
            if node.contains_key(word[i]):
                node = node.get(word[i])
            else:
                break

        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)

        return node is not None and node.is_end()

    def starts_with(self, prefix: str) -> bool:

        node = self.search_prefix(prefix)
        return node is not None

    def search_longest_prefix(self, word: str) -> str:
        node = self.root
        prefix = []

        for i in range(len(word)):
            if node.contains_key(word[i]) and node.get_links() == 1 and not node.is_end():
                prefix.append(word[i])
                node = node.get(word[i])
            else:
                break

        return ''.join(prefix)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]

        trie = Trie()

        for i in range(len(strs)):
            trie.insert(strs[i])

        return trie.search_longest_prefix(strs[0])
