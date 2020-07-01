class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])

        if x + 1 == y == z - 1:
            min_steps = 0
        elif y - x > 2 and z - y > 2:
            min_steps = 2
        else:
            min_steps = 1

        max_steps = z - x - 2

        return [min_steps, max_steps]
