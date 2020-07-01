from bisect import bisect


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted([w.count(min(w)) for w in words])
        return [len(f) - bisect(f, q.count(min(q))) for q in queries]
