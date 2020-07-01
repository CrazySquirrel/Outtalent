class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1: return -1

        indeg = [0] * (N + 1)
        outdeg = [0] * (N + 1)

        for a, b in trust:
            outdeg[a] += 1
            indeg[b] += 1

        for i in range(1, len(indeg)):
            if outdeg[i] == 0 and indeg[i] == N - 1: return i

        return -1
