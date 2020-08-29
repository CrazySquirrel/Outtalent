class Solution:
    keyboard = {
        'A': (0, 0), 'B': (1, 0), 'C': (2, 0), 'D': (3, 0), 'E': (4, 0), 'F': (5, 0),
        'G': (0, 1), 'H': (1, 1), 'I': (2, 1), 'J': (3, 1), 'K': (4, 1), 'L': (5, 1),
        'M': (0, 2), 'N': (1, 2), 'O': (2, 2), 'P': (3, 2), 'Q': (4, 2), 'R': (5, 2),
        'S': (0, 3), 'T': (1, 3), 'U': (2, 3), 'V': (3, 3), 'W': (4, 3), 'X': (5, 3),
        'Y': (0, 4), 'Z': (1, 4)
    }

    def minimumDistance(self, word: str) -> int:
        l = len(word)

        if l <= 2: return 0

        @lru_cache(None)
        def distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        @lru_cache(None)
        def count(p1x, p1y, p2x, p2y, i):
            if i >= l: return 0

            p3x, p3y = Solution.keyboard[word[i]]

            if p2x is None and p2y is None:
                return min(
                    distance(p1x, p1y, p3x, p3y) + count(p3x, p3y, p2x, p2y, i + 1),
                    count(p1x, p1y, p3x, p3y, i + 1)
                )
            else:
                return min(
                    distance(p1x, p1y, p3x, p3y) + count(p3x, p3y, p2x, p2y, i + 1),
                    distance(p2x, p2y, p3x, p3y) + count(p1x, p1y, p3x, p3y, i + 1)
                )

        p1x, p1y = Solution.keyboard[word[0]]

        return count(p1x, p1y, None, None, 1)
