class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) == 0: return True
        if len(typed) < len(name): return False

        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]

        if len(g1) != len(g2): return False

        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))
