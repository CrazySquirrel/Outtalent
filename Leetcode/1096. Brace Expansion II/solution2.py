class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        cur = []
        stack = []
        res = []
        for c in expression:
            if c.isalpha():
                cur = [k + c for k in cur or ['']]
            elif c == "{":
                stack.append(res)
                stack.append(cur)
                res, cur = [], []
            elif c == "}":
                pre = stack.pop()
                preRes = stack.pop()
                cur = [p + c for c in res + cur for p in pre or ['']]
                res = preRes
            elif c == ",":
                res += cur
                cur = []
        return sorted(set(res + cur))
