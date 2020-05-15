class Solution:
    def increase(self, rating: List[int], start: int, pref: int, count: int) -> int:
        if count == 3: return 1

        result = 0

        for i in range(start, len(rating)):
            if rating[i] > pref:
                result += self.increase(rating, i + 1, rating[i], count + 1)

        return result

    def decrease(self, rating: List[int], start: int, pref: int, count: int) -> int:
        if count == 3: return 1

        result = 0

        for i in range(start, len(rating)):
            if rating[i] < pref:
                result += self.decrease(rating, i + 1, rating[i], count + 1)

        return result

    def numTeams(self, rating: List[int]) -> int:
        return self.increase(rating, 0, 0, 0) + self.decrease(rating, 0, 10 ** 5 + 1, 0)
