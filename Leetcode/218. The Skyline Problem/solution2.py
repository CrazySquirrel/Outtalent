class segTree():
    def __init__(self, n):
        self.tree = [0] * n

    def update(self, index, start, end, left, right, value):
        if left > right or right < start or left > end: return

        if start == left and end == right:
            self.tree[index] = max(self.tree[index], value)
            return

        mid = (start + end) // 2
        self.update(index * 2, start, mid, left, min(mid, right), value)
        self.update(index * 2 + 1, mid + 1, end, max(mid + 1, left), right, value)

    def query(self, index, start, end, i):
        if start == end: return self.tree[index]

        mid = (start + end) // 2

        if i <= mid:
            res = self.query(index * 2, start, mid, i)
        else:
            res = self.query(index * 2 + 1, mid + 1, end, i)

        return max(res, self.tree[index])


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        indices = set()
        for s, e, h in buildings:
            indices.add(s)
            indices.add(e)
        indices = sorted(list(indices))

        index2id = {n: i for i, n in enumerate(indices)}

        END = len(indices) - 1

        st = segTree(len(indices) * 4)
        for s, e, h in buildings: st.update(1, 0, END, index2id[s], index2id[e] - 1, h)

        pre = 0
        res = []

        for i in range(END + 1):
            h = st.query(1, 0, END, i)
            if h != pre: res.append([indices[i], h])
            pre = h

        return res
