class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dic = Counter(nums)

        def isSquare(x):
            if sqrt(x) == int(sqrt(x)):
                return True
            return False
        res = 1 if dic[1] <= 1 else dic[1] if dic[1] % 2 == 1 else dic[1] - 1
        for i in dic:
            if isSquare(i):
                tmp = i
                cnt = 1
                while isSquare(tmp) and tmp != 1:
                    tmp = int(sqrt(tmp))
                    if dic[tmp] >= 2:
                        cnt += 2

                res = max(cnt, res)
        return res
