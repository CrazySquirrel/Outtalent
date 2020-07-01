class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        max_size = result = 0

        groups = {}

        for i in range(1, n + 1):
            s = sum_digits(i)

            if s not in groups: groups[s] = []

            groups[s].append(i)
            size = len(groups[s])

            if size > max_size:
                max_size = size
                result = 1
            elif size == max_size:
                result += 1

        return result
