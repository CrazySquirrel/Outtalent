class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for h in range(12):
            hc = bin(h).count('1')
            if hc == num: result.append('%d:00' % (h))
            if hc >= num: continue
            for m in range(1, 60):
                if hc + bin(m).count('1') == num:
                    result.append('%d:%02d' % (h, m))
        return result
