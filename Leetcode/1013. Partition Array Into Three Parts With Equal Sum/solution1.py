class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)

        if total % 3 != 0: return False

        target = total // 3
        count = accumulate = 0

        for i in range(len(A)):
            accumulate += A[i]

            if accumulate == target:
                count += 1
                accumulate = 0

                if count == 2: break

        return count == 2 and i < len(A) - 1
