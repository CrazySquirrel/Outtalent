class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []

        counter = 0
        for a in A:
            counter = (counter << 1) | a
            result.append(counter % 5 == 0)

        return result
