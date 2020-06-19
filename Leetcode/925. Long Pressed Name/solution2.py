class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) == 0: return True
        if len(typed) < len(name): return False

        a, b = len(name), len(typed)
        i, j = 0, 0

        while j < b:
            if i == a:
                if typed[j] != name[a - 1]: return False
            else:
                if typed[j] != name[i] and (j == 0 or typed[j] != typed[j - 1]): return False
                if typed[j] == name[i]: i += 1
            j += 1

        if i != a: return False

        return True
