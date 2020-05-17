class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S: return []

        r = S.rfind(S[0])
        i = 0

        while i < r:
            r = max(r, S.rfind(S[i]))
            i += 1

        return [r + 1] + self.partitionLabels(S[r + 1:])
