class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        l1 = len(version1)
        l2 = len(version2)

        if l1 < l2:
            version1.extend([0] * (l2 - l1))
        elif l1 > l2:
            version2.extend([0] * (l1 - l2))

        for i in range(max(l1, l2)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1

        return 0
