class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = []

        for s in S:
            result.append(s)

            while len(result) > 1 and result[-2] == result[-1]:
                result.pop()
                result.pop()

        return ''.join(result)
