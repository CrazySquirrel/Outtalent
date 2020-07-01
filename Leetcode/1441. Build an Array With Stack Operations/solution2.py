class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        for i in range(1, max(target) + 1):
            result.append("Push")
            if i not in target: result.append("Pop")
        return result
