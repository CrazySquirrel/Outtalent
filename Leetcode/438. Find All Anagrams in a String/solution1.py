from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_l = len(p)
        s_l = len(s)

        if p_l > s_l: return []

        p_counter = Counter(p)
        s_counter = Counter(s[:p_l - 1])

        result = []

        for i in range(p_l - 1, s_l):
            c1 = s[i]
            c2 = s[i - p_l + 1]

            s_counter[c1] += 1
            if s_counter == p_counter: result.append(i - p_l + 1)

            s_counter[c2] -= 1
            if s_counter[c2] == 0: del s_counter[c2]

        return result
