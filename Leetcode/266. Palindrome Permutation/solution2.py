class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count_odd = 0
        for v in Counter(s).values():
            if v % 2 == 0: continue
            count_odd += 1
            if count_odd > 1: return False
        return True
