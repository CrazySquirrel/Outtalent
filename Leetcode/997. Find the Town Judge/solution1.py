class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1: return 1

        counter = collections.Counter()

        for f, t in trust:
            counter[f] -= 1
            counter[t] += 1

        for k, v in counter.items():
            if v == N - 1: return k

        return -1
