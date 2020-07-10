class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [n for n, f in counter[:k]]
