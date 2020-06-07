class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            num_to_str = ''
            if i % 3 == 0: num_to_str += 'Fizz'
            if i % 5 == 0: num_to_str += 'Buzz'
            if not num_to_str: num_to_str = str(i)
            result.append(num_to_str)
        return result
