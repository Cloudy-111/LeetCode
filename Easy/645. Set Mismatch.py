class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {}
        n = len(nums)
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        res = []
        for i in range(1, n + 1):
            if i not in dic:
                res.append([i, 2])
            if i in dic:
                if dic[i] == 2:
                    res.append([i, 1])
        return [k for k, v in sorted(res, key=lambda x: x[1])]
