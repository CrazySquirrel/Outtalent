class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_appearence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_appearence[stack[-1]]:
                    char = stack.pop()
                    seen.remove(char)

                stack.append(c)
                seen.add(c)

        return ''.join(stack)
