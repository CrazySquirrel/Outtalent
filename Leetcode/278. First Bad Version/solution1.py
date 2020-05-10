# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l, h = 1, n

        while l < h:
            m = l + (h - l) // 2

            if isBadVersion(m):
                h = m - 1
            else:
                l = m + 1

        return l if isBadVersion(l) else l + 1
