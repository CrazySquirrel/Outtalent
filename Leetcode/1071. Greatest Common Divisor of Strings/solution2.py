class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        t1 = len(str1)
        t2 = len(str2)

        t = self.gcd(t1, t2)

        if len(str1) > len(str2):
            if str1 == str2 + str1[:t1 - t2]:
                return str1[:t]
            else:
                return ""

        if len(str1) < len(str2):
            if str2 == str1 + str2[:t2 - t1]:
                return str2[:t]
            else:
                return ""

        if str1 == str2:
            return str1[:t]
        else:
            return ""
