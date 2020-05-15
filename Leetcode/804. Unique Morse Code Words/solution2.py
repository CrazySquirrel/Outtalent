MORZE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set([''.join(MORZE[ord(w) - 97] for w in word) for word in words]))
