class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for log in logs:
            if log == './':
                pass
            elif log == '../':
                if result > 0:
                    result -= 1
            else:
                result += 1
        return result
