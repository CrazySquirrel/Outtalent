class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0

        words = []
        word = []

        for c in text:
            if c == ' ':
                if word:
                    words.append(''.join(word))
                    word = []
                spaces += 1
            else:
                word.append(c)

        if word:
            words.append(''.join(word))

        l = len(words) - 1

        if l <= 0:
            return ''.join(words) + ' ' * spaces

        spaces_between = spaces // l
        spaces_end = spaces - spaces_between * l

        return (' ' * spaces_between).join(words) + ' ' * spaces_end
