class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1: return [1]

        level = 1
        start = 2
        end = 4

        while end <= label:
            start = end
            end *= 2
            level += 1

        path = []

        for i in range(level):
            mid = start + (end - start) // 2

            if label >= mid:
                start = mid
                path.append('L' if level % 2 == 1 else 'R')
            else:
                end = mid
                path.append('R' if level % 2 == 1 else 'L')

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
