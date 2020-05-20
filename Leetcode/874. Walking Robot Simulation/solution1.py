class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        position_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        x, y, direction, max_distance = 0, 0, 0, 0
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                x_off, y_off = position_offset[direction]
                for i in range(command):
                    if (x + x_off, y + y_off) in obstacles: break
                    x += x_off
                    y += y_off
                max_distance = max(max_distance, x ** 2 + y ** 2)
        return max_distance
