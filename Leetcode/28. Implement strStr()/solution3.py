class Solution:
    def hashing(self, S: str) -> int:
        l = len(S)
        return sum([ord(S[i]) * (self.base1 ** (l - 1 - i)) for i in range(l)])

    def rolling_hashing(self, old_hash: int, old_value: str, new_value: int) -> int:
        return (old_hash - ord(old_value) * self.base2) * self.base1 + ord(new_value)

    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        self.base1 = 401
        self.base2 = self.base1 ** (n - 1)

        n_hash = self.hashing(needle)
        m_hash = self.hashing(haystack[0:n])

        if m_hash == n_hash: return 0

        for i in range(1, m - n + 1):
            m_hash = self.rolling_hashing(m_hash, haystack[i - 1], haystack[i + n - 1])
            if m_hash == n_hash: return i

        return -1
