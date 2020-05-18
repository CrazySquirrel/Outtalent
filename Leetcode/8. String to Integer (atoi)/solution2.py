import re

INT_MAX = (1 << 31) - 1
INT_MIN = -1 << 31


class Solution:
    def myAtoi(self, S: str) -> int:
        if not S: return 0

        start = 0
        end = len(S)

        # find start
        for i in range(len(S)):
            if S[i] != ' ':
                start = i
                break

        # check if it's valid start
        if S[start] != '-' and S[start] != '+' and not S[start].isdigit():
            return 0

        sign = 1

        # check fo sign
        if S[start] == '-' or S[start] == '+':
            sign = -1 if S[start] == '-' else 1
            start += 1

        # check if it's valid digit
        if start == len(S) or not S[start].isdigit():
            return 0

        # find end
        for i in range(start, len(S)):
            if not S[i].isdigit():
                end = i
                break

        return min(INT_MAX, max(INT_MIN, sign * int(S[start:end])))
