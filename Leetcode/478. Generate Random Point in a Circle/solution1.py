from random import random
from math import sqrt, cos, sin, pi


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        nr = sqrt(random()) * self.r
        alpha = random() * 2 * pi
        newx = self.x + nr * cos(alpha)
        newy = self.y + nr * sin(alpha)
        return [newx, newy]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
