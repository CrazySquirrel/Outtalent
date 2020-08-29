class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0: return str(n)
        result = []
        for i in range(1, int(log10(n)) + 2):
            result.append(str(n % 10))
            n //= 10
            if n and i % 3 == 0: result.append('.')
        return ''.join(result[::-1])
