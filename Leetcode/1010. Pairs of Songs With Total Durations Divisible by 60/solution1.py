class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count_arr = [0] * 60
        result = 0
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60
            result += count_arr[complement]
            count_arr[remainder] += 1
        return result
