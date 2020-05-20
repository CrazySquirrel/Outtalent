class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words): return False
        w_to_p = {}
        p_to_w = {}
        for i, w in enumerate(words):
            if pattern[i] not in p_to_w: p_to_w[pattern[i]] = w
            if w not in w_to_p: w_to_p[w] = pattern[i]
            if p_to_w[pattern[i]] != w or w_to_p[w] != pattern[i]: return False
        return True
