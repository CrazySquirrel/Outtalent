from typing import List
from math import atan2, pi


class Solution:
    @staticmethod
    def get_polar_angle(pole: List[int], point: List[int]) -> float:
        if point == pole: return -inf

        delta_x = point[0] - pole[0]
        delta_y = point[1] - pole[1]

        polar_angle = atan2(delta_y, delta_x)

        if polar_angle < 0: polar_angle += 2 * pi

        return polar_angle

    @staticmethod
    def get_bottom_left_point(points: List[List[int]]) -> List[int]:
        bottom_left_point = [float("inf"), float("inf")]

        for point in points:
            is_lower = (point[1] < bottom_left_point[1])
            is_as_low = (point[1] == bottom_left_point[1])
            is_to_the_left = (point[0] < bottom_left_point[0])

            if is_lower or (is_as_low and is_to_the_left): bottom_left_point = point

        return bottom_left_point

    @staticmethod
    def get_triangle_area(point1: List[int], point2: List[int], point3: List[int]) -> float:
        prod1 = (point1[0] - point3[0]) * (point2[1] - point1[1])
        prod2 = (point1[0] - point2[0]) * (point3[1] - point1[1])

        triangle_area = .5 * abs(prod1 - prod2)

        return triangle_area

    @staticmethod
    def is_left_turn(point1: List[int], point2: List[int], point3: List[int]) -> bool:
        vector1 = (point2[0] - point1[0], point2[1] - point1[1])
        vector2 = (point3[0] - point2[0], point3[1] - point2[1])

        return vector1[0] * vector2[1] - vector2[0] * vector1[1] > 0

    def get_convex_hull(self, points: List[List[int]]) -> List[List[int]]:
        pole = self.get_bottom_left_point(points)

        points.sort(key=lambda point: self.get_polar_angle(pole, point))

        convex_hull: List[List[int]]
        stack: List[List[int]]
        convex_hull = stack = []

        for point in points:
            while len(stack) >= 2:
                triple = (stack[-2], stack[-1], point)
                if not self.is_left_turn(*triple):
                    stack.pop()
                else:
                    break
            stack.append(point)

        return convex_hull

    def largestTriangleArea(self, points: List[List[int]]) -> float:

        convex_hull = self.get_convex_hull(points)
        convex_hull_length = len(convex_hull)

        max_triangle_area = 0.

        for idx1 in range(convex_hull_length - 2):
            for idx2 in range(idx1 + 1, convex_hull_length - 1):
                for idx3 in range(idx2 + 1, convex_hull_length):
                    triangle_area = self.get_triangle_area(convex_hull[idx1], convex_hull[idx2], convex_hull[idx3])
                    max_triangle_area = max(max_triangle_area, triangle_area)

        return max_triangle_area
