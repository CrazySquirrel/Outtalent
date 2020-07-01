from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = Counter(A[0])

        for i in range(1, len(A)):
            counter = Counter(A[i])
            tmp = Counter()
            for k in result:
                result[k] = min(result[k], counter[k])
                if result[k] > 0: tmp[k] = result[k]
            result = tmp

        ans = []

        for k, v in result.items():
            ans.extend([k] * v)

        return ans
