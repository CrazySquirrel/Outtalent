class Solution:
    result = {}

    def toHex(self, num: int) -> str:
        if 0 <= num < 10: return str(num)
        if 10 <= num < 16: return chr(ord('a') + num - 10)
        if num in self.result: return self.result[num]
        if num < 0:
            self.result[num] = self.toHex(2 ** 32 + num)
        else:
            self.result[num] = self.toHex(num // 16) + self.toHex(num % 16)
        return self.result[num]
