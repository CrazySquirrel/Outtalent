class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteLetters = set(list(ransomNote))
        for l in noteLetters:
            if magazine.count(l) < ransomNote.count(l):
                return False
        return True
