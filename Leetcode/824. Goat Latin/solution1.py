class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = {"a", "e", "i", "o", "u"}

        return ' '.join([(word if word[0].lower() in s else word[1:] + word[0]) + 'ma' + 'a' * (i + 1) for i, word in
                         enumerate(S.split(' '))])
