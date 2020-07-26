class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        if k >= len(s) - 1: return k
        freqs = collections.defaultdict(int)
        max_freq = i = j = 0
        for j in range(len(s)):
            freqs[s[j]] += 1
            max_freq = max(freqs[s[j]], max_freq)
            if max_freq + k < j - i + 1:
                freqs[s[i]] -= 1
                i += 1
        return j - i + 1
