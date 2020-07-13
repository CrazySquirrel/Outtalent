class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        out = []

        for d in num:
            while k and out and out[-1] > d:
                k -= 1
                out.pop()
            out.append(d)

        return "".join(out[:-k or None]).lstrip('0') or '0'
