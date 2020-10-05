class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        h = {'q': 0, 'Q': 0, 'w': 0, 'W': 0, 'e': 0, 'E': 0, 'r': 0, 'R': 0, 't': 0, 'T': 0, 'y': 0, 'Y': 0, 'u': 0,
             'U': 0, 'i': 0, 'I': 0, 'o': 0, 'O': 0, 'p': 0, 'P': 0, 'a': 1, 'A': 1, 's': 1, 'S': 1, 'd': 1, 'D': 1,
             'f': 1, 'F': 1, 'g': 1, 'G': 1, 'h': 1, 'H': 1, 'j': 1, 'J': 1, 'k': 1, 'K': 1, 'l': 1, 'L': 1, 'z': 2,
             'Z': 2, 'x': 2, 'X': 2, 'c': 2, 'C': 2, 'v': 2, 'V': 2, 'b': 2, 'B': 2, 'n': 2, 'N': 2, 'm': 2, 'M': 2}
        return filter(lambda word: all([h[c] == h[word[0]] for c in word]), words)
