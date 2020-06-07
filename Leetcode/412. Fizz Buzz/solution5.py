class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [str(i) for i in range(n + 1)]
        for i in range(3, n + 1, 3): result[i] = 'Fizz'
        for i in range(5, n + 1, 5): result[i] = 'Buzz'
        for i in range(15, n + 1, 15): result[i] = 'FizzBuzz'
        return result[1:]
