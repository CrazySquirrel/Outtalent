class Solution:
    def checkRecord(self, s: str) -> bool:
        return 'LLL' not in s and s.count('A') < 2
