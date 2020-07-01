class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count(c) // 'balloon'.count(c) for c in 'balon')
