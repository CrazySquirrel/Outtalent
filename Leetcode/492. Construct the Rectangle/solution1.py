class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L = int(math.ceil(Math.sqrt(area)))
        while area % L != 0: L += 1
        W = int(area / L)
        return [L, W]
