class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ret = []
        right_up_points = []

        for building in buildings:
            left, right, height = building

            while len(right_up_points) != 0 and right_up_points[-1][1] < left:
                _, ret_left = right_up_points.pop()
                ret_height = 0 if len(right_up_points) == 0 else right_up_points[-1][0]
                ret.append([ret_left, ret_height])

            if not right_up_points:
                ret.append([left, height])
                right_up_points.append([height, right])
                continue

            if height > right_up_points[-1][0]:
                if ret and left == ret[-1][0] and height > ret[-1][1]: ret.pop()
                ret.append([left, height])

            new_idx = bisect.bisect_left(right_up_points, [height, right])
            while new_idx != 0 and right_up_points[new_idx - 1][1] <= right:
                right_up_points.pop(new_idx - 1)
                new_idx -= 1

            if new_idx == len(right_up_points) or right_up_points[new_idx][1] < right:
                right_up_points.insert(new_idx, [height, right])

        while len(right_up_points) != 0:
            _, ret_left = right_up_points.pop()
            ret_height = 0 if len(right_up_points) == 0 else right_up_points[-1][0]
            ret.append([ret_left, ret_height])

        return ret
