class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        colors = []
        lens = []
        for col in boxes:
            if colors and colors[-1] == col:
                lens[-1] += 1
            else:
                colors.append(col)
                lens.append(1)

        @lru_cache(None)
        def dp(i, j, boxCount):
            if i == j: return (boxCount + lens[i]) ** 2
            if i > j: return 0
            ret = (boxCount + lens[i]) ** 2 + dp(i + 1, j, 0)
            for nxt in range(i + 1, j + 1):
                if colors[nxt] == colors[i]:
                    ret = max(ret, dp(i + 1, nxt - 1, 0) + dp(nxt, j, boxCount + lens[i]))
            return ret

        return dp(0, len(colors) - 1, 0)
