import string


class Solution:
    def removeDuplicates(self, S: str) -> str:
        dup = {2 * ch for ch in string.ascii_lowercase}
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in dup: S = S.replace(d, '')
        return S
