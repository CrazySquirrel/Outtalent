class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i).count('1') for i in range(num + 1)]
