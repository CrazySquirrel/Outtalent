class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cerry = 1
        for i in range(len(digits) - 1, -1, -1):
            cerry += digits[i]
            digits[i] = cerry % 10
            cerry //= 10
            if not cerry: break
        else:
            if cerry: digits.insert(0, cerry)
        return digits
