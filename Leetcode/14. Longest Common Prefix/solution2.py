class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]

        strs.sort()

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]: return strs[0][:i]

        return strs[0] if len(strs[0]) < len(strs[-1]) else strs[-1]
