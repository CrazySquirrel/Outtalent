class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        for i in range(len(A)):
            A[i] = even.pop() if i % 2 == 0 else odd.pop()
        return A
