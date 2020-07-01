class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = collections.Counter(arr1)

        result = []

        for num in arr2:
            if num in counter:
                result.extend([num] * counter[num])
                del counter[num]

        other = []

        for num, freq in counter.items():
            other.extend([num] * freq)

        return result + sorted(other)
