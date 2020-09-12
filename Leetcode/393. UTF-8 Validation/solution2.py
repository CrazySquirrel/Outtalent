class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for d in data:
            if (0b10 << 6) <= d <= ((0b11 << 6) - 1):
                if not count: return False
                count -= 1
            else:
                if count: return False
                if d < (0b1 << 7):
                    continue
                elif d < (0b111 << 5):
                    count = 1
                elif d < (0b1111 << 4):
                    count = 2
                elif d < (0b11111 << 3):
                    count = 3
                else:
                    return False
        return count == 0
