class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        @lru_cache(None)
        def isValid(s: str) -> bool:
            left = 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    left -= 1
                    if left < 0: return False
            return left == 0

        result = []

        @lru_cache(None)
        def dfs(s: str):
            nonlocal result
            if not s or isValid(s):
                if result:
                    if len(result[0]) > len(s): return
                    if len(result[0]) < len(s): result = []
                result.append(s)
                return

            for i in range(len(s)):
                if s[i] == '(' or s[i] == ')':
                    dfs(s[:i] + s[i + 1:])

        dfs(s)

        return result
