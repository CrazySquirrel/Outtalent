class Solution:
    def judgeCircle(self, m: str) -> bool:
        return m.count('U') == m.count('D') and m.count('R') == m.count('L')
