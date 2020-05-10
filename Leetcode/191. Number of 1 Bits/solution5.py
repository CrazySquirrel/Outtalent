TABLE8 = [0] * 2 ** 8

for index in range(len(TABLE8)):
    TABLE8[index] = (index & 1) + TABLE8[index >> 1]


class Solution:
    def hammingWeight(self, n: int) -> int:
        return TABLE8[n & 0xff] + TABLE8[(n >> 8) & 0xff] + TABLE8[(n >> 16) & 0xff] + TABLE8[n >> 24]
