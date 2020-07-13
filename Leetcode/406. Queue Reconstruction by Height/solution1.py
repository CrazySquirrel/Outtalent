class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])): res.insert(p[1], p)
        return res
