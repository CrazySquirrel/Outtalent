import re


class Solution:
    def helper(self, expression: str) -> List[str]:
        s = re.search("\{([^}{]+)\}", expression)

        if not s: return {expression}

        g = s.group(1)

        result = set()

        for c in g.split(','):
            result |= self.helper(expression.replace('{' + g + '}', c, 1))

        return result

    def braceExpansionII(self, expression: str) -> List[str]:
        return sorted(list(self.helper(expression)))
