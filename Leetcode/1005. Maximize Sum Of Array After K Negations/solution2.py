class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A, ncnt = sorted(A), sum([1 for a in A if a < 0])
        cnt1, cnt2 = min(K, ncnt), K - ncnt if K > ncnt else 0
        for i in range(cnt1): A[i] = -A[i]
        return sum(A) - min(A) * 2 * (cnt2 % 2) if cnt2 else sum(A)
