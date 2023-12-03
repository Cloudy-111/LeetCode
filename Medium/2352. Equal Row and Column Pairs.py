class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic1 = {}
        for i in grid:
            tmp = '.'.join([str(x) for x in i])
            tmp += '.'
            if tmp not in dic1:
                dic1[tmp] = 1
            else:
                dic1[tmp] += 1
        dic2 = {}
        for i in range(len(grid[0])):
            tmp = ''
            for j in range(len(grid)):
                tmp += str(grid[j][i]) + '.'
            if tmp not in dic2:
                dic2[tmp] = 1
            else:
                dic2[tmp] += 1
        res = 0
        for i in dic1:
            if i in dic2:
                res += dic1[i] * dic2[i]
        return res
