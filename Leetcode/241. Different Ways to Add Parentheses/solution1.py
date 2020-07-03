class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        result = []
        for i in range(len(input)):
            if input[i] == "+" or input[i] == "-" or input[i] == "*":
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i + 1:])
                for left in lefts:
                    for right in rights:
                        if input[i] == "+":
                            result.append(left + right)
                        elif input[i] == "-":
                            result.append(left - right)
                        elif input[i] == "*":
                            result.append(left * right)
        if not result: result.append(int(input))
        return result
