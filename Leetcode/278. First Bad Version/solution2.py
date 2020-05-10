# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        if n == 1: return 1

        l, h = 1, n - 1

        while l <= h:
            m = l + (h - l) // 2
            curr = isBadVersion(m)
            next = isBadVersion(m + 1)
            if curr and m == 1:
                return 1
            if not curr and next:
                return m + 1
            if curr and next:
                h = m - 1
            else:
                l = m + 1
