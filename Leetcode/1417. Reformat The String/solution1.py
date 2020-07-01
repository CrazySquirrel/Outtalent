class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        numbers = []

        for c in s:
            if c.isalpha():
                letters.append(c)
            else:
                numbers.append(c)

        if abs(len(letters) - len(numbers)) > 1: return ''

        result = []

        while letters and numbers:
            result.append(letters.pop())
            result.append(numbers.pop())

        if letters: result.append(letters.pop())
        if numbers: result.insert(0, numbers.pop())

        return ''.join(result)
