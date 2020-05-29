# Further Thoughts / Follow up

Let's take a look at a slightly different problem:

Given a set of keys S = [S<sup>1</sup>, S<sup>2</sup> ... S<sup>n</sup>], find the longest common prefix among a string q and S. 
This LCP query will be called frequently.

We could optimize LCP queries by storing the set of keys S in a Trie. For more information about Trie, please see this 
article Implement a trie (Prefix trie). In a Trie, each node descending from the root represents a common prefix of some keys. 
But we need to find the longest common prefix of a string q and all key strings. This means that we have to find the deepest 
path from the root, which satisfies the following conditions:

* it is prefix of query string q
* each node along the path must contain only one child element. Otherwise the found path will not be a common prefix among all strings.
* the path doesn't comprise of nodes which are marked as end of key. Otherwise the path couldn't be a prefix a of key which is shorter than itself.

## Algorithm

The only question left, is how to find the deepest path in the Trie, that fulfills the requirements above. 
The most effective way is to build a trie from [S<sup>1</sup>...S<sup>n</sup>] strings. 
Then find the prefix of query string q in the Trie. We traverse the Trie from the root, till it is impossible to 
continue the path in the Trie because one of the conditions above is not satisfied.

![](4.png)

```python
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
```

## Complexity Analysis

In the worst case query q has length m and it is equal to all n strings of the array.

* Time complexity : preprocessing O(S), where S is the number of all characters in the array, LCP query O(m).

Trie build has O(S) time complexity. To find the common prefix of q in the Trie takes in the worst case O(m).

* Space complexity : O(S). We only used additional S extra space for the Trie.

[Prev](solution5.md)