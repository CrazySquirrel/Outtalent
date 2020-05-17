class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}

        l = r = 0

        result = []

        for i, c in enumerate(S):
            l = max(l, last[c])
            if i == l:
                result.append(i - r + 1)
                r = i + 1

        return result
