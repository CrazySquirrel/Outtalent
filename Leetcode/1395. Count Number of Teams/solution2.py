from bisect import bisect


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def insert(x):
            i = bisect(tmp, x)
            tmp.insert(i, x)
            return i

        tmp = []
        lower = list(map(insert, rating))

        tmp = []
        upper = list(map(insert, rating[::-1]))[::-1]

        counter = 0

        total_length = len(rating)
        index_length = total_length - 1

        for i, (l, u) in enumerate(zip(lower, upper)):
            counter += l * (index_length - i - u)
            counter += u * (i - l)

        return counter
