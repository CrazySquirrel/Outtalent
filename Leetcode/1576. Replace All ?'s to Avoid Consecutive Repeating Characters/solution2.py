class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        l = len(s)
        if l == 1:
            if s[0] == '?': s[0] = 'a'
        else:
            if s[0] == '?': s[0] = list({'a', 'b', 'c'} - {s[1]})[0]
            if s[-1] == '?': s[-1] = list({'a', 'b', 'c'} - {s[-2]})[0]
        for i in range(1, l - 1):
            if s[i] != '?': continue
            s[i] = list({'a', 'b', 'c'} - {s[i - 1], s[i + 1]})[0]
        return ''.join(s)
