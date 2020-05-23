from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums: hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1: return i
