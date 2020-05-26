from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        d = defaultdict(int)

        for i, c in enumerate(secret):
            if c == guess[i]:
                bulls += 1
            else:
                d[c] += 1

        for i, c in enumerate(guess):
            if c != secret[i] and c in d and d[c] > 0:
                cows += 1
                d[c] -= 1

        return str(bulls) + "A" + str(cows) + "B"
