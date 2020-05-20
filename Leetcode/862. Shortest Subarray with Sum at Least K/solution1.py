from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        dp = [0] * (len(A) + 1)

        for i in range(1, len(dp)): dp[i] = dp[i - 1] + A[i - 1]

        res = len(A) + 1

        q = deque()

        for i in range(len(dp)):
            while q and dp[i] - dp[q[0]] >= K: res = min(res, i - q.popleft())
            while q and dp[i] < dp[q[-1]]: q.pop()
            q.append(i)

        return res if res != len(A) + 1 else -1
