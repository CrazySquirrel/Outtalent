from itertools import permutations


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        if not all([word in s for word in words]): return []
        result = set()
        for substring in permutations(words):
            substring = ''.join(substring)
            start = 0
            while True:
                try:
                    start = s.index(substring, start)
                    result.add(start)
                    start += 1
                except ValueError as e:
                    break
        return result
