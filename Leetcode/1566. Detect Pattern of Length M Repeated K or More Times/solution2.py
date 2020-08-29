class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m + 1):
            if i + k * m <= len(arr) and arr[i:i + k * m] == arr[i:i + m] * k: return True
        return False
