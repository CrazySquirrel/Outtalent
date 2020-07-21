class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(path):
            if len(path) == 2 * n:
                if valid(path):
                    result.append("".join(path))
            else:
                path.append('(')
                generate(path)
                path.pop()
                path.append(')')
                generate(path)
                path.pop()

        def valid(path):
            counter = 0
            for c in path:
                if c == '(':
                    counter += 1
                else:
                    counter -= 1
                if counter < 0: return False
            return counter == 0

        result = []

        generate([])

        return result
