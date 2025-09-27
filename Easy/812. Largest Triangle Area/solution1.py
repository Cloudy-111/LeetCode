class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = max(
            abs(self.cross(a, b, c)) / 2
            for a, b, c in combinations(points, 3)
        )
        return res

    def cross(self, A, B, C):
        return (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])
