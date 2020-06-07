H = [[0], [1, 2, 4, 8], [3, 5, 6, 9, 10], [7, 11]]
M = [[0], [1, 2, 4, 8, 16, 32], [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48],
     [7, 11, 13, 14, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44, 49, 50, 52, 56],
     [15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58], [31, 47, 55, 59]]


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for i in range(max(0, num - 5), min(4, num + 1)):
            for h in H[i]:
                for m in M[num - i]:
                    result.append('%d:%02d' % (h, m))
        return result
