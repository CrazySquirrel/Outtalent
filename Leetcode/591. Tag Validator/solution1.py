from re import sub


class Solution:
    def isValid(self, code: str) -> bool:
        code = sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = None
        while prev != code:
            prev = code
            code = sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'
