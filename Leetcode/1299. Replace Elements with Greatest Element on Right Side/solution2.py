class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        m = -1
        for i in range(len(a) - 1, -1, -1):
            a[i], m = m, max(m, a[i])
        return a
