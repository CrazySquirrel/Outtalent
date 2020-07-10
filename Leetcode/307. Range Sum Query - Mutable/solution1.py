class NumArray:
    nums = None
    tree = None
    n = 0

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0 for _ in range(self.n + 1)]
        self.nums = [0 for _ in range(self.n)]
        for i in range(self.n): self.update(i, nums[i])

    def update(self, i: int, val: int) -> None:
        if self.n == 0: return

        diff = val - self.nums[i]
        self.nums[i] = val
        j = i + 1

        while j <= self.n:
            self.tree[j] += diff
            j += (j & -j)

    def sumRange(self, i: int, j: int) -> int:
        return self.getSum(j + 1) - self.getSum(i)

    def getSum(self, i: int) -> int:
        total = 0

        while i > 0:
            total += self.tree[i]
            i -= (i & -i)

        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
