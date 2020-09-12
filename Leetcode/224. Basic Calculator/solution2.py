class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        zero = ord('0')
        operand = 0
        res = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + ord(ch) - zero
            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append((sign, res))
                sign = 1
                res = 0
            elif ch == ')':
                prev_sign, prev_res = stack.pop()
                res = prev_sign * (res + sign * operand) + prev_res
                operand = 0
        return res + sign * operand
