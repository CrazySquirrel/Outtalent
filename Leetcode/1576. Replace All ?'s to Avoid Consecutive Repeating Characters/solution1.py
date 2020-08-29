class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        l = len(s)
        for i in range(l):
            if s[i] != '?': continue
            s[i] = list({'a', 'b', 'c'} - {s[i - 1] if i > 0 else '', s[i + 1] if i < l - 1 else ''})[0]
        return ''.join(s)
