class Solution:
    h = {'a': 'bc', 'b': 'ac', 'c': 'ab'}

    def getHappyString(self, n: int, k: int) -> str:
        # Calculating the total number of happy strings of length n
        total = 3 * (2 ** (n - 1))

        # If K grater then total then we can return an empty string
        if k > total: return ''

        # We determine which third K falls into A B or C
        step = total // 3

        if k <= step:
            result = 'a'
        elif k <= step * 2:
            result = 'b'
            k -= step
        else:
            result = 'c'
            k -= step * 2

        # Next for each step we look at which half the current k falls into A or B and use correct letter
        for i in range(n, 1, -1):
            # Total number of happy substring is 2 ** (i - 1) and we need middle
            step = 2 ** (i - 2)

            if 0 < k <= step:
                result += Solution.h[result[-1]][0]
            else:
                result += Solution.h[result[-1]][1]
                k -= step

        return result
