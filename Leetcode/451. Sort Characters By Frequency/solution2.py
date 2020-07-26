class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        return ''.join(c * counts[c] for c in sorted(counts, key=counts.get, reverse=True))
