class Fenwick:
    def __init__(self, n):
        self.n = n
        self.val = [0] * n

    def query(self, i):
        s = 0
        while i > 0:
            s += self.val[i]
            i -= i & -i
        return s

    def update(self, i, delta):
        while i < self.n:
            self.val[i] += delta
            i += i & -i


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        pos = [i + m for i in range(m + 1)]

        tree = Fenwick(2 * m + 1)

        for i in range(1, m + 1):
            tree.update(i + m, 1)

        result = []

        for query in queries:
            result.append(tree.query(pos[query] - 1))

            tree.update(pos[query], -1)

            pos[query] = m
            m -= 1

            tree.update(pos[query], 1)

        return result
