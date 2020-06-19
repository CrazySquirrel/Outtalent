h = {
    '+': lambda a, b: b + a,
    '-': lambda a, b: b - a,
    '*': lambda a, b: b * a,
    '/': lambda a, b: abs(b) // abs(a) * (1 if (b >= 0 and a >= 0) or (b <= 0 and a <= 0) else -1)
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in h:
                stack.append(h[c](stack.pop(), stack.pop()))
            else:
                stack.append(int(c))
        return stack[-1]
