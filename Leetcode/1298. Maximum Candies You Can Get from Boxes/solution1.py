class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        if not initialBoxes: return 0
        if 1 not in status: return 0
        boxes = []
        result = 0
        while True:
            flag = False
            for b in initialBoxes:
                if status[b] == 1:
                    flag = True
                    result += candies[b]
                    boxes += containedBoxes[b]
                    for j in keys[b]: status[j] = 1
                    initialBoxes.remove(b)
            initialBoxes += boxes
            boxes = []
            if not flag: break
        return result
