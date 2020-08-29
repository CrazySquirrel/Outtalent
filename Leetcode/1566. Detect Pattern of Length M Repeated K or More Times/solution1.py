class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(m):
            value = []
            counter = 0
            for j in range(i, len(arr) - i, m):
                new_value = arr[j:j + m]
                if value != new_value:
                    value = new_value
                    counter = 1
                else:
                    counter += 1
                if counter >= k: return True
        return False
