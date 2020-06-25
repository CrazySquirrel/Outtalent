class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        lens = len(A) + len(B)

        def kth(ai: int, al: int, bi: int, bl: int, k: int):
            while True:
                if al - ai < 0: return B[k + bi]
                if bl - bi < 0: return A[k + ai]
                if k < 1: return min(A[k + ai], B[k + bi])
                am, bm = (ai + al) // 2, (bi + bl) // 2
                av, bv = A[am], B[bm]
                if (am - ai) + (bm - bi) < k:
                    if av > bv:
                        k = k - (bm - bi) - 1
                        bi = bm + 1
                    else:
                        k = k - (am - ai) - 1
                        ai = am + 1
                else:
                    if av > bv:
                        al = am - 1
                    else:
                        bl = bm - 1

        if lens % 2 == 1:
            return kth(0, len(A) - 1, 0, len(B) - 1, lens // 2)
        else:
            return (kth(0, len(A) - 1, 0, len(B) - 1, lens // 2) + kth(0, len(A) - 1, 0, len(B) - 1, lens // 2 - 1)) / 2
