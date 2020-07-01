class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        prev = 1
        for n in target:
            if prev != i: result.extend(['Push', 'Pop'] * (n - prev))
            result.append('Push')
            prev = n + 1
        return result
