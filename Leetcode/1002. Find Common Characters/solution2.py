class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        for i, val in enumerate(A[0]):
            if not all(val in string for string in A[1:]): continue
            for i in range(1, len(A)): A[i] = A[i].replace(val, '', 1)
            result.append(val)
        return result
