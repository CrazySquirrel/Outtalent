class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                return False
            else:
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        return all(x == '*' for x in p[p_idx:])
