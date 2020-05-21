class Solution:
    def countAndSay(self, n: int) -> str:
        result = [1]
        for _ in range(n - 1):
            next = []
            for num in result:
                if not next or next[-1] != num:
                    next += [1, num]
                else:
                    next[-2] += 1
                result = next
        return "".join(map(str, result))
