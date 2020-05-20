class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]

        strs.sort()
        result = []

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                result.append(strs[0][i])
            else:
                break
        return "".join(result)
