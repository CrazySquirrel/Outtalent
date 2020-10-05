class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        l = len(S)

        h = [i for i, v in enumerate(S) if v == C]
        h.append(l * 2)

        result = []
        j = 0

        for i in range(l):
            if i > h[j]: j += 1
            if j == 0:
                result.append(h[j] - i)
            else:
                result.append(min(i - h[j - 1], h[j] - i))

        return result
