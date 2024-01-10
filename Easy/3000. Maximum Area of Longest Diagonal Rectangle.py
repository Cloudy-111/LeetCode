class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        def calDiagonal(h, w):
            return h * h + w * w
        res = 0
        for i in range(len(dimensions)):
            h, w = dimensions[i]
            d = calDiagonal(h, w)
            if d > res or (d == res and h * w > area):
                res = d
                area = h * w

        return area
