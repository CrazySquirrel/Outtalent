class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                pre_op = each
                num = 0
        return sum(stack)

    def addOperators(self, num: str, target: int) -> List[str]:
        if not num: return []

        result = []

        s = {'+', '-', '*'}
        l = len(num)

        def dfs(i: int, prefix: str):
            if i == l:
                if self.calculate(prefix) == target: result.append(prefix)
            else:
                for c in s: dfs(i + 1, prefix + c + num[i])

                if prefix[-1] == '0' and (len(prefix) == 1 or prefix[-2] in s): return

                dfs(i + 1, prefix + num[i])

        dfs(1, num[0])

        return result
