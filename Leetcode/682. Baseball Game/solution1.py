class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for o in ops:
            if o == '+':
                stack.append(stack[-1] + stack[-2])
            elif o == 'C':
                stack.pop()
            elif o == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(o))
        return sum(stack)
