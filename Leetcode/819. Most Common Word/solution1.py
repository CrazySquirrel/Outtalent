import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)

        words = re.findall(r'\w+', paragraph.lower())

        return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]
