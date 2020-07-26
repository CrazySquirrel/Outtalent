class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def dfs(used: int, val: int) -> bool:
            for i in range(maxChoosableInteger, 0, -1):
                if (1 << i) & used == 0:
                    if val + i >= desiredTotal:
                        return True
                    elif not dfs(used | (1 << i), val + i):
                        return True
            return False

        total = (1 + maxChoosableInteger) * maxChoosableInteger // 2

        if total <= desiredTotal:
            return total == desiredTotal and maxChoosableInteger & 0x1

        return dfs(1, 0)
