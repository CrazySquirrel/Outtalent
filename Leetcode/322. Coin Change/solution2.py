class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n, result = len(coins), amount + 1

        def dfs(x, t, cn):
            nonlocal result

            if cn + t // coins[x] >= result: return

            if t % coins[x] == 0:
                result = cn + t // coins[x]
                return

            if x == n - 1: return

            for i in range(t // coins[x], -1, -1):
                dfs(x + 1, t - coins[x] * i, cn + i)

        dfs(0, amount, 0)
        return -1 if result > amount else result
