class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_count = sum([c.isupper() for c in word])
        return upper_count == len(word) or upper_count == 0 or upper_count == 1 and word[0].isupper()
