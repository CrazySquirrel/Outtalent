class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)

        @lru_cache(None)
        def increasing(prev: int, i: int, c: int):
            if c == 0: return 1
            if i == l: return 0
            result = 0
            for j in range(i, l):
                if rating[j] <= prev: continue
                result += increasing(rating[j], j + 1, c - 1)
            return result

        @lru_cache(None)
        def decreasing(prev: int, i: int, c: int):
            if c == 0: return 1
            if i == l: return 0
            result = 0
            for j in range(i, l):
                if rating[j] >= prev: continue
                result += decreasing(rating[j], j + 1, c - 1)
            return result

        return increasing(-inf, 0, 3) + decreasing(inf, 0, 3)
