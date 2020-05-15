import bisect


class Solution:
    def sortString(self, s: str) -> str:
        string = sorted(list(s))
        result = []

        while string:
            c = 'a'

            i = bisect_left(string, c)
            if i == len(string): break
            c = string.pop(i)
            result.append(c)

            while True:
                i = bisect_right(string, c)
                if i == len(string): break
                c = string.pop(i)
                result.append(c)

            i = bisect_right(string, c)
            if not i: break
            c = string.pop(i - 1)
            result.append(c)

            while True:
                i = bisect_left(string, c)
                if not i: break
                c = string.pop(i - 1)
                result.append(c)

        return ''.join(result)
