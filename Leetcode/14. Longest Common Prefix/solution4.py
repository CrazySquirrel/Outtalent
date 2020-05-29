class Solution:
    def isCommonPrefix(self, strs: List[str], l: int) -> bool:
        prefix = strs[0][:l]
        for i in range(1, len(strs)):
            if strs[i].find(prefix) != 0:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        l, h = 1, min([len(s) for s in strs])
        while l <= h:
            m = l + (h - l) // 2
            if self.isCommonPrefix(strs, m):
                l = m + 1
            else:
                h = m - 1
        return strs[0][:l + (h - l) // 2]
