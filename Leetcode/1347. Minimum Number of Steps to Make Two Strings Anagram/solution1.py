class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr = [0] * 26
        for i in range(len(s)):
            arr[ord(s[i]) - 97] += 1
            arr[ord(t[i]) - 97] -= 1
        counter = 0
        for a in arr:
            if a > 0: counter += a
        return counter
