class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        m = 0
        for i in a:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            m = max(dic[i], m)
        print(dic)
        res = []
        while m > 0:
            a = []
            for i in dic:
                if dic[i] > 0:
                    a.append(i)
                    dic[i] -= 1
            res.append(a)
            m -= 1
        return res
