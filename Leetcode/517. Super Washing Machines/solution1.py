class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines) % len(machines): return -1
        avg = sum(machines) / len(machines)
        result = total = 0
        for m in machines:
            total += m - avg
            result = max(result, abs(total), m - avg)
        return int(result)
