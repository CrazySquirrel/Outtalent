class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""

        for c in address:
            if c == ".":
                result += "[.]"
            else:
                result += c

        return result
