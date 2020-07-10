from bisect import bisect_right, insort_right


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        sum_area = 0

        tx1 = ty1 = inf
        tx2 = ty2 = -inf

        lines = []

        for x1, y1, x2, y2 in rectangles:
            sum_area += (x2 - x1) * (y2 - y1)

            tx1 = min(tx1, x1)
            ty1 = min(ty1, y1)
            tx2 = max(tx2, x2)
            ty2 = max(ty2, y2)

            lines.append((x1, True, y1, y2))
            lines.append((x2, False, y1, y2))

        total_area = (tx2 - tx1) * (ty2 - ty1)

        if sum_area != total_area: return False

        bst = []
        for line in sorted(lines):
            x, flag, bottom, top = line
            if flag:
                i = bisect_right(bst, (bottom, top))
                insort_right(bst, (bottom, top))

                if i + 1 < len(bst) and bst[i + 1][0] < bst[i][1] or i > 0 and bst[i][0] < bst[i - 1][1]: return False
            else:
                bst.remove((bottom, top))

        return True
