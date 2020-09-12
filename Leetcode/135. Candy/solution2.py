class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1: return len(ratings)

        def count(n: int) -> int:
            return (n * (n + 1)) // 2

        candies = up = down = old_slope = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            elif ratings[i] < ratings[i - 1]:
                new_slope = -1
            else:
                new_slope = 0

            if (old_slope > 0 and new_slope == 0) or (old_slope < 0 <= new_slope):
                candies += count(up) + count(down) + max(up, down)
                up = down = 0

            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1
            elif new_slope == 0:
                candies += 1

            old_slope = new_slope

        candies += count(up) + count(down) + max(up, down) + 1

        return candies
