class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for i, c in enumerate(s): result[indices[i]] = c
        return ''.join(result)
