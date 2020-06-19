class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        result = 0

        for seat, group in itertools.groupby(seats):
            if seat: continue
            K = len(list(group))
            result = max(result, (K + 1) // 2)

        return max(result, seats.index(1), seats[::-1].index(1))
