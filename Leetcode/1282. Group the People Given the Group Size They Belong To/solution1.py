class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        h = {}

        for i in range(len(groupSizes)):
            size = groupSizes[i]

            if not size in h:
                h[size] = [[]]

            if len(h[size][-1]) == size:
                h[size].append([])

            h[size][-1].append(i)

        return sorted(reduce(lambda x, y: x + y, h.values()), key=len)
