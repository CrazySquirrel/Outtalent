class Solution:
    def myAtoi(self, S: str) -> int:
        if not S: return 0

        NUM_SET = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        SIGN_SET = {'-', '+'}
        NUM_START_SET = SIGN_SET | NUM_SET

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        INT_OVERFLOW = 214748364

        ZERO = ord('0')

        i = 0

        while i < len(S) and S[i] == ' ': i += 1

        if i == len(S) or S[i] not in NUM_START_SET: return 0

        is_negative = S[i] == '-'

        if S[i] in SIGN_SET: i += 1

        if i == len(S) or S[i] not in NUM_SET: return 0

        res = 0

        while i < len(S) and S[i] in NUM_SET:
            digit = ord(S[i]) - ZERO

            if is_negative:
                if res > INT_OVERFLOW or (res == INT_OVERFLOW and digit > 8): return INT_MIN
            else:
                if res > INT_OVERFLOW or (res == INT_OVERFLOW and digit > 7): return INT_MAX

            res = res * 10 + digit

            i += 1

        return -res if is_negative else res
