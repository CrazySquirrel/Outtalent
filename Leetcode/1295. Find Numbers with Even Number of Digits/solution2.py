class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0

        for num in nums:
            n, c = 9, 1

            while n < num:
                n = n * 10 + 9
                c += 1

            if c % 2 == 0:
                counter += 1

        return counter
