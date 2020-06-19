class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l: int, r: int, k: int) -> int:
            m = l + (r - l) // 2

            nums[m], nums[r] = nums[r], nums[m]

            pivot = nums[r]
            index = l

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
            nums[index], nums[r] = nums[r], nums[index]

            if index == k:
                return nums[k]
            elif index > k:
                return partition(l, index - 1, k)
            else:
                return partition(index + 1, r, k)

        return partition(0, len(nums) - 1, len(nums) - k)
