class TrieNode:
    def __init__(self):
        self.links = {}
        self.end = False

    def contains_key(self, c: str) -> bool:
        return c in self.links

    def get_links(self) -> int:
        return len(self.links)

    def get(self, c: str) -> "TrieNode":
        return self.links[c]

    def put(self, c: str, node: "TrieNode") -> None:
        self.links[c] = node

    def set_end(self) -> None:
        self.end = True

    def is_end(self) -> bool:
        return self.end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if not node.contains_key(w): node.put(w, TrieNode())
            node = node.get(w)
        node.set_end()

    def search_prefix(self, word: str) -> "TrieNode":
        node = self.root
        for w in word:
            if not node.contains_key(w): break
            node = node.get(w)
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end()

    def start_with(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None

    def search_longest_prefix(self, word: str) -> str:
        node = self.root
        prefix = ''
        for w in word:
            if node.contains_key(w) and node.get_links() == 1 and not node.is_end():
                prefix += w
                node = node.get(w)
            else:
                break
        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]

        trie = Trie()
        for s in strs: trie.insert(s)

        return trie.search_longest_prefix(strs[0])
