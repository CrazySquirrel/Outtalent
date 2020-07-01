class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination < start: start, destination = destination, start
        s = sum(distance[start:destination])
        return min(s, sum(distance) - s)
