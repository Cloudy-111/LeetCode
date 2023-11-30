from ast import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        lst = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums[i])):
                sumRowCol = i + j
                row = i
                tmp = (sumRowCol, row, nums[i][j])
                lst.add(tmp)

        lst = sorted(lst, key=lambda x: (x[0], -x[1]))
        for i in lst:
            res.add(i[2])

        return res
