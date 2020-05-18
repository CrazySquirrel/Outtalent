class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if A == B:
            s = set()
            for a in A:
                if a in s:
                    return True
                s.add(a)
            return False

        pair = False

        for i in range(len(A)):
            if A[i] != B[i]:
                if not pair:
                    pair = (A[i], B[i])
                elif pair == (B[i], A[i]):
                    pair = True
                else:
                    return False

        return pair == True
