class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        h = {}
        for word in A:
            key = ''.join(sorted(word[::2]) + sorted(word[1::2]))
            if key not in h: h[key] = []
            h[key].append(word)
        return len(h)
