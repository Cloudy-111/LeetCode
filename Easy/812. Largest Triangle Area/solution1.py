class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0.0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    area = self.calArea(points[i], points[j], points[k])
                    res = max(res, area)
        return res
    
    def calArea(self, pointA, pointB, pointC):
        return abs((pointB[0] - pointA[0]) * (pointC[1] - pointA[1]) - (pointC[0] - pointA[0]) * (pointB[1] - pointA[1])) / 2