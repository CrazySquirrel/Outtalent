class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        result = counter = 0

        for c in S:
            counter += 1 if c == '(' else -1
            if counter == -1:
                counter += 1
                result += 1

        return result + counter
