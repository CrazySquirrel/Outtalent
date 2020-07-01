class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1: return 1

        counter = collections.Counter()
        result = set(range(1, N + 1))

        for f, t in trust:
            counter[f] -= 1
            counter[t] += 1
            if f in result: result.remove(f)

        if len(result) != 1: return -1

        result = list(result)[0]

        return result if counter[result] == N - 1 else -1
