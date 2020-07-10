class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        n = 0
        for e in b: n = (n * 10 + e) % 1140
        return pow(a, n, 1337)
