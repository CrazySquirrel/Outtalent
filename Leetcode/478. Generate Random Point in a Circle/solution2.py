from random import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        while True:
            rx = (random() - 0.5) * 2
            ry = (random() - 0.5) * 2
            if ((rx ** 2) + (ry ** 2)) <= 1: break
        return [rx * self.radius + self.xc, ry * self.radius + self.yc]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
