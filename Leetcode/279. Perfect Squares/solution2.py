class Solution:
    def numSquares(self, n: int) -> int:
        lst = [i * i for i in range(1, int(n ** 0.5) + 1)]

        result = 0

        remains = {n}

        while remains:
            result += 1
            tmp = set()

            for remain in remains:
                for e in lst:
                    if remain < e: break
                    if remain == e: return result
                    tmp.add(remain - e)

            remains = tmp

        return result
