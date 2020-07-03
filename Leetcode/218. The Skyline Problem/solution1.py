from heapq import heappop, heappush


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append([l, -h, r])
            events.append([r, 0, -1])
        events.sort()

        result, hp = [], [(0, inf)]

        for l, h, r in events:
            while l >= hp[0][1]: heappop(hp)

            if h: heappush(hp, (h, r))

            if not result or result[-1][1] != -hp[0][0]:
                result.append([l, -hp[0][0]])

        return result
