class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        if l1 == 0: return str2
        if l1 < l2: return self.gcdOfStrings(str2, str1)
        if str1[0:l2] != str2: return ""
        return self.gcdOfStrings(str1[l2:], str2)
