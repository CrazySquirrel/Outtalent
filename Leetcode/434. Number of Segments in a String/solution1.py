import re


class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        return len(re.split('\s+', s))
