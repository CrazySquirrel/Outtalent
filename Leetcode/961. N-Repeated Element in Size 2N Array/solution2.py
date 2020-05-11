import random


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        while True:
            v1, v2 = random.sample(A, 2)

            if v1 == v2:
                return v1
