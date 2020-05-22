class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b): b = '0' * (len(a)-len(b)) + b
        if len(a) < len(b): a = '0' * (len(b)-len(a)) + a
        c , i = '0', 0
        result = ''
        for i in range(len(a)-1,-1,-1):
            if a[i] == '1' and b[i] == '1':
                if c == '1':
                    result = '1' + result
                else:
                    result = '0' + result
                c = '1'
            elif a[i] == '1' or b[i] == '1':
                if c == '1':
                    result = '0' + result
                    c = '1'
                else:
                    result = '1' + result
                    c = '0'
            else:
                if c == '1':
                    result = '1' + result
                else:
                    result = '0' + result
                c = '0'
            i += 1
        if c == '1':
            result = '1' + result
        return result