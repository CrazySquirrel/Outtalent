class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        return ''.join(sorted(list(s), key=lambda x: (counter[x], x), reverse=True))
