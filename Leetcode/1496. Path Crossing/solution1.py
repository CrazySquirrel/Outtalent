class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = {(0, 0)}
        x = y = 0

        for p in path:
            if p == 'N':
                y -= 1
            elif p == 'S':
                y += 1
            elif p == 'W':
                x -= 1
            else:
                x += 1

            if (x, y) in s: return True

            s.add((x, y))

        return False
