class Solution:
    def reformat(self, s: str) -> str:
        p1, p2 = [], []

        for char in s:
            if char.isalpha():
                p1.append(char)
            else:
                p2.append(char)

        l1, l2 = len(p1), len(p2)

        if l1 < l2: p1, p2 = p2, p1
        if abs(l1 - l2) > 1: return ''

        return ''.join([p2[i // 2] if i % 2 else p1[i // 2] for i in range(l1 + l2)])
