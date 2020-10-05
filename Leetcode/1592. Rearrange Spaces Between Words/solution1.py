class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = list(filter(lambda t: bool(t), text.split(' ')))
        if len(words) <= 1: return ''.join(words) + ' ' * spaces
        between = spaces // (len(words) - 1)
        atend = spaces - between * (len(words) - 1)
        return (' ' * between).join(words) + ' ' * atend
