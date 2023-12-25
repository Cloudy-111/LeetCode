import math


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        moveX = [1, 1, 1, 0, 0, -1, -1, -1]
        moveY = [1, 0, -1, 1, -1, 1, 0, -1]
        n = len(img)
        m = len(img[0])
        res = []
        for i in range(n):
            tmp = []
            for j in range(m):
                cnt = 1
                sum = img[i][j]
                for k in range(8):
                    newX = i + moveX[k]
                    newY = j + moveY[k]
                    if newX >= 0 and newX < n and newY >= 0 and newY < m:
                        sum += img[newX][newY]
                        cnt += 1
                tmp.append(math.floor(sum / cnt))
            res.append(tmp)
        return res
