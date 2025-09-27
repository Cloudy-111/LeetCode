class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        convex = self.convex_hull(points)
        res = max(
            abs(self.cross(a, b, c)) / 2
            for a, b, c in combinations(convex, 3)
        )
        return res

    def convex_hull(self, points):
        lower_hull = []
        for point in points:
            while len(lower_hull) > 2 and self.cross(lower_hull[-1], lower_hull[-2], point) < 0:
                lower_hull.pop()
            lower_hull.append(point)

        upper_hull = []
        for point in reversed(points):
            while len(upper_hull) > 2 and self.cross(upper_hull[-1], upper_hull[-2], point) < 0:
                upper_hull.pop()
            upper_hull.append(point)

        return lower_hull[:-1] + upper_hull[:-1]

    def cross(self, A, B, C):
        return (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])
