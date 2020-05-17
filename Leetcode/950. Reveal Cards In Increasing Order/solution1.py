class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = []
        for card in sorted(deck)[::-1]:
            result = [card] + result[-1:] + result[:-1]
        return result
