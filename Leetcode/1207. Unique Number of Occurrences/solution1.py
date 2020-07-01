class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()
        for v in collections.Counter(arr).values():
            if v in s: return False
            s.add(v)
        return True
