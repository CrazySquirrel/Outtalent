class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == num:
                    result.append('%d:%02d' % (h, m))
        return result
