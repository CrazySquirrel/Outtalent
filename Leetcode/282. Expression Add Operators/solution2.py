class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num: return []

        N, res = len(num), []

        def dfs(i, prev_operand, cur_operand, value, path):
            if i == N:
                if value == target and cur_operand == 0: res.append(path)
                return

            cur_operand = cur_operand * 10 + int(num[i])
            str_op = str(cur_operand)

            if cur_operand > 0:
                dfs(i + 1, prev_operand, cur_operand, value, path)

            if path:
                dfs(i + 1, cur_operand, 0, value + cur_operand, path + "+" + str_op)
            else:
                dfs(i + 1, cur_operand, 0, value + cur_operand, str_op)
                return

            dfs(i + 1, -cur_operand, 0, value - cur_operand, path + "-" + str_op)

            value = value - prev_operand + (cur_operand * prev_operand)

            dfs(i + 1, cur_operand * prev_operand, 0, value, path + "*" + str_op)

        dfs(0, 0, 0, 0, "")

        return res
