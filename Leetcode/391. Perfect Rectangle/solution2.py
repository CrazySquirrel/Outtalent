class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        lx, ly, rx, ry = inf, inf, -inf, -inf

        corner = set()
        area = 0

        for x1, y1, x2, y2 in rectangles:
            if x1 <= lx and y1 <= ly:
                lx, ly = x1, y1

            if x2 >= rx and y2 >= ry:
                rx, ry = x2, y2

            area += (y2 - y1) * (x2 - x1)
            corner ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}

        return corner == {(rx, ry), (lx, ly), (lx, ry), (rx, ly)} and area == (rx - lx) * (ry - ly)
