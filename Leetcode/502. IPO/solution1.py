class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        num = sorted([x for x in zip(Profits, Capital)])
        for _ in range(min(k, len(num))):
            i = len(num) - 1
            while i >= 0 and num[i][1] > W: i -= 1
            if i < 0: break
            W += num[i][0]
            num.pop(i)
        return W
