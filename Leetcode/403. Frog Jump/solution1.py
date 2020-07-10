class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) <= 1: return True
        if stones[1] != 1:  return False
        max_step = {s: set() for s in stones}
        max_step[1].add(1)
        for s in stones[1:-1]:
            for j in max_step[s]:
                for jump in (j - 1, j, j + 1):
                    if jump > 0 and s + jump in max_step:
                        max_step[s + jump].add(jump)
        return len(max_step[stones[-1]]) > 0
