from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        result = deque([deck.pop()])

        while deck:
            result.append(result.popleft())
            result.append(deck.pop())

        return reversed(result)
