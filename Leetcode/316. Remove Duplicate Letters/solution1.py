class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        h = Counter()

        for c in s: h[c] += 1

        stack = list()
        visited = set()

        for c in s:
            h[c] -= 1;

            if c in visited:
                continue
            else:
                visited.add(c)

            while len(stack) > 0 and c < stack[-1] and h[stack[-1]] > 0:
                visited.remove(stack[-1])
                stack.pop()

            stack.append(c)
            visited.add(c)

        return ''.join(stack)
