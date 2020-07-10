class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = collections.defaultdict(int)
        for w in words:
            mask = reduce(lambda s, c: s | (1 << (ord(c) - 97)), set(w), 0)
            d[mask] = max(d[mask], len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
