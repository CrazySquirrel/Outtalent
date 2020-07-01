from bisect import insort


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if y > x: insort(stones, y - x)
        return stones[-1] if stones else 0
