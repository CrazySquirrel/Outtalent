class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        h = {v: i for i, v in enumerate(list1)}
        result = []
        m = inf
        for i, v in enumerate(list2):
            if v in h:
                r = h[v] + i
                if r < m:
                    m = r
                    result = [v]
                elif r == m:
                    result.append(v)
        return result
