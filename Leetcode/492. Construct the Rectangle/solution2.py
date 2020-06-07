class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(math.sqrt(area))
        while W > 0:
            if area % W == 0:
                return [area // W, W]
            else:
                W -= 1
