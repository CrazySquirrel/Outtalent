class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        a = b = 0
        result = []
        for c in seq:
            if c == '(':
                result.append(a)
                a ^= 1
            else:
                result.append(b)
                b ^= 1
        return result
