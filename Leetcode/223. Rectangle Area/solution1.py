class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        ((A, B), (C, D)), ((E, F), (G, H)) = sorted([((A, B), (C, D)), ((E, F), (G, H))])

        rectangle1_area = (D - B) * (C - A)
        rectangle2_area = (H - F) * (G - E)

        x, y = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))

        overlap_area = x * y if x > 0 and y > 0 else 0

        return rectangle1_area + rectangle2_area - overlap_area
