class Solution:
    def helper(self, s: str, d: int) -> List[str]:
        if len(s) > 3 * d or len(s) < d: return []

        result = []

        for i in range(min(3, len(s))):
            cur = s[:i + 1]

            if (len(cur) >= 2 and cur[0] == '0') or int(cur) > 255: continue

            if d > 1:
                for postfix in self.helper(s[i + 1:], d - 1):
                    result.append([cur] + postfix)
            elif cur == s:
                result.append([cur])

        return result

    def restoreIpAddresses(self, s: str) -> List[str]:
        return ['.'.join(ip) for ip in self.helper(s, 4)]
