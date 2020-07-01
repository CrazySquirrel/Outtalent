class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        T = collections.Counter([i % 60 for i in time])
        return sum([T[i] * T[60 - i] for i in range(1, 30)]) + (T[0] * (T[0] - 1) + T[30] * (T[30] - 1)) // 2
