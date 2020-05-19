from collections import Counter
from fractions import gcd


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        group_size = counter[deck[0]]

        for i in counter:
            group_size = gcd(group_size, counter[i])
            if group_size < 2: return False

        return True
