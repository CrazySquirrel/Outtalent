class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4: return []

        result = []

        def dfs(s, path):
            if not s and len(path) == 4:
                result.append('.'.join(path))
            for i in range(1, 4):
                if i > len(s): continue
                number = int(s[:i])
                if str(number) == s[:i] and number <= 255:
                    dfs(s[i:], path + [s[:i]])

        dfs(s, [])
        return result
