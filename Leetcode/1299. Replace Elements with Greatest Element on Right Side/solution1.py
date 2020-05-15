class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = [-1]

        for i in range(len(arr) - 1, -1, -1):
            right.append(max(right[-1], arr[i]))

        return right[::-1][1:]
