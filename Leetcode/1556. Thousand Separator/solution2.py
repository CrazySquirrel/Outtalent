class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0: return str(n)
        l = int(log10(n)) + 1
        l = l + ceil(l / 3) - 1
        result = ['.'] * l
        i = j = 0
        while n:
            result[l - i - 1] = str(n % 10)
            n //= 10
            i += 1
            j += 1
            if n and j % 3 == 0: i += 1
        return ''.join(result)
