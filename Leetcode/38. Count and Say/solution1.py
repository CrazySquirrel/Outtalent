class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n - 1):
            j = 0
            new = ''
            while j < len(res):
                count = 1
                while j < len(res) - 1 and res[j] == res[j + 1]:
                    count += 1
                    j += 1
                j += 1
                new += str(count) + res[j - 1]
            res = new
        return res
