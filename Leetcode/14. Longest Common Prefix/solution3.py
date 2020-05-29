class Solution:
    def commonPrefix(self, left: str, right: str) -> str:
        m = min(len(left), len(right))
        for i in range(m):
            if left[i] != right[i]:
                return left[:i]
        return left[:m]

    def helper(self, strs: List[str], l: int, r: int) -> str:
        if l == r: return strs[l]
        m = l + (r - l) // 2
        lcp_left = self.helper(strs, l, m)
        lcp_right = self.helper(strs, m + 1, r)
        return self.commonPrefix(lcp_left, lcp_right)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        return self.helper(strs, 0, len(strs) - 1)
