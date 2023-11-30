from ast import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = 0
        for i in candies:
            m = max(m, candies[i])
        res = []
        for i in candies:
            if i + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res
