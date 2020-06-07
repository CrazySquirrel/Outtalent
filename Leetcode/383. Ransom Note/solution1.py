from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        for c in note_counter:
            if c not in magazine_counter or note_counter[c] > magazine_counter[c]:
                return False
        return True
