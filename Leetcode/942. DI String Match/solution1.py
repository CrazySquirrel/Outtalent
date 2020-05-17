class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i, j = 0, len(S)
        result = []
        for c in S:
            if c == 'I':
                result.append(i)
                i += 1
            else:
                result.append(j)
                j -= 1
        result.append(i)
        return result
