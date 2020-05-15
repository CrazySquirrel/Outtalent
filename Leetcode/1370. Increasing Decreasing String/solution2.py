from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        data = dict(Counter(s))
        seq = sorted(data.keys())
        result = ''
        while sum(data.values()) > 0:
            for i in seq:
                if data[i] > 0:
                    result += i
                    data[i] -= 1
            for i in seq[::-1]:
                if data[i] > 0:
                    result += i
                    data[i] -= 1
        return result
