from collections import defaultdict
from bisect import bisect


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        locs = defaultdict(list)
        ring_len = len(ring)

        for i in range(-ring_len, 2 * ring_len):
            c = ring[(i + ring_len) % ring_len]
            locs[c].append(i)

        @lru_cache(None)
        def dfs(pr: int, pk: int) -> int:
            if pk == len(key):
                return 0
            elif ring[(pr + len(ring)) % len(ring)] == key[pk]:
                return 1 + dfs(pr, pk + 1)
            else:
                p1 = bisect(locs[key[pk]], pr)

                left, right = locs[key[pk]][p1 - 1], locs[key[pk]][p1]

                l_dist, r_dist = pr - left, right - pr

                left = (left + len(ring)) % len(ring)
                right = (right + len(ring)) % len(ring)

                return 1 + min(l_dist + dfs(left, pk + 1), r_dist + dfs(right, pk + 1))

        return dfs(0, 0)
