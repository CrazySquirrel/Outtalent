class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        result = 0

        for path in input.split('\n'):
            count = path.count('\t')

            while count < len(stack): stack.pop()

            if stack:
                stack.append(len(path) - count + stack[-1])
            else:
                stack.append(len(path) - count)

            if '.' in path:
                result = max(result, stack[-1] + len(stack) - 1)

        return result
