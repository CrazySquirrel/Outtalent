from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        counter = Counter(text)
        return min([counter[k] // balloon[k] for k in balloon])
