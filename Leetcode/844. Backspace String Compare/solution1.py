class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def g(s: str):
            skip = 0
            for c in s[::-1]:
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c

        return all(s == t for s, t in zip_longest(g(S), g(T)))
