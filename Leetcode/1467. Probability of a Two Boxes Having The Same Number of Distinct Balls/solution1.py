from itertools import permutations


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        setOfBalls = []
        currentBall = 1

        for b in balls:
            setOfBalls.extend([currentBall] * b)
            currentBall += 1

        equal = 0
        total = 0

        for choice in permutations(setOfBalls, len(setOfBalls)):
            half = len(choice) // 2
            if len(set(choice[:half])) == len(set(choice[half:])): equal += 1
            total += 1

        return equal / total
