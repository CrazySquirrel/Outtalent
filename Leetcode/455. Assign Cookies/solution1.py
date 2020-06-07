class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = result = 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j += 1
            else:
                result += 1
                i += 1
                j += 1
        return result
