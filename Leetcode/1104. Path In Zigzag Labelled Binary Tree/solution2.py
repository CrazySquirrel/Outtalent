from math import ceil, log2


class Solution:
    ### Calculate tree level and level range (list 1-1, 2-4, 4-8, 8-16, 16-32 and etc)
    def labelLavel(self, label: int) -> List[int]:
        level = ceil(log2(label))

        if 2 ** level != label: level -= 1

        start = 2 ** level
        end = start * 2

        return [level, start, end]

    ### Based ont tree level and start - end range get turns from root to label in tree
    def getTurns(self, level: int, start: int, end: int, label: int) -> List[str]:
        # If current tree level is reversed we need to calculate turns in reversed
        L = 'L' if level % 2 == 1 else 'R'
        R = 'R' if level % 2 == 1 else 'L'

        turns = []

        for i in range(level):
            mid = start + (end - start) // 2

            if label >= mid:
                start = mid
                turns.append(L)
            else:
                end = mid
                turns.append(R)

        return turns

    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1: return [1]

        level, start, end = self.labelLavel(label)

        path = self.getTurns(level, start, end, label)

        result = [1]

        rights = []
        level = 1
        start = 2
        end = 4

        for p in path:
            if p == 'R': rights.append(1)

            index = sum(rights) if rights else 0

            if level % 2 == 1:
                result.append(end - 1 - index)
            else:
                result.append(start + index)

            rights = [r * 2 for r in rights]

            start = end
            end *= 2
            level += 1

        return result
