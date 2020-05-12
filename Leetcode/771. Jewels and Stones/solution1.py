class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        h = set(list(J))

        counter = 0

        for s in S:
            if s in h:
                counter += 1

        return counter
