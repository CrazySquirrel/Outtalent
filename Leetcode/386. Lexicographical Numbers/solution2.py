class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        current = 1
        result = []
        for i in range(n):
            result.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                if current >= n: current //= 10
                current += 1
                while current % 10 == 0: current //= 10
        return result
