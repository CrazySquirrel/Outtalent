class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l, i = len(bits), 0
        while i < l:
            if i < l - 1:
                if bits[i] == 1:
                    i += 2
                else:
                    i += 1
            else:
                return bits[i] == 0
        return False
