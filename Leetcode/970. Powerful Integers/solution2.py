class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2: return []

        powers_of_x = [1]

        if x != 1:
            while True:
                power_of_x = x * powers_of_x[-1]
                if power_of_x >= bound: break
                powers_of_x.append(power_of_x)

        powers_of_y = [1]

        if y != 1:
            while True:
                power_of_y = y * powers_of_y[-1]
                if power_of_y >= bound: break
                powers_of_y.append(power_of_y)

        result = set()
        for power_of_x in powers_of_x:
            for power_of_y in powers_of_y:
                total = power_of_x + power_of_y
                if total <= bound: result.add(total)

        return result
