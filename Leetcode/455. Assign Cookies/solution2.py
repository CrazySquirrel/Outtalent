class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = result = 0
        for c in g:
            while i < len(s) and c > s[i]: i += 1
            if i == len(s): break
            result += 1
            i += 1
        return result
