class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        totalCnt = len(s)

        lowers = [c for c in s if c.islower()]
        uppers = [c for c in s if c.isupper()]
        digits = [c for c in s if c.isdigit()]

        typeCnt = bool(lowers) + bool(uppers) + bool(digits)

        clist = []
        li, lc = 0, (s[0] if s else None)
        for i, c in enumerate(s):
            if c != lc:
                clist.append((lc, li, i - 1))
                li, lc = i, c
        clist.append((lc, li, totalCnt - 1))

        repeats = [y - x + 1 for c, x, y in clist if y - x > 1]

        if totalCnt < 6:
            if max(repeats + [0]) == 5:
                return max(2, 3 - typeCnt)
            return max(6 - totalCnt, 3 - typeCnt)

        deleteCnt = max(totalCnt - 20, 0)

        heap = [(r % 3, r) for r in repeats]

        heapq.heapify(heap)
        while heap and totalCnt > 20:
            mod, r = heapq.heappop(heap)
            delta = min(mod + 1, totalCnt - 20)
            totalCnt -= delta
            heapq.heappush(heap, (2, r - delta))

        changeCnt = sum(r // 3 for mod, r in heap)

        return deleteCnt + max(changeCnt, 3 - typeCnt)
