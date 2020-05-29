class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]

        w1, w2 = min(strs), max(strs)

        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]: return w1[:i]

        return w1 if len(w1) < len(w2) else w2
