class Solution:
    # bài này không khó, chỉ cần đếm tần suất của các số trong dãy, với mỗi số lần N biẻu diễn thành 3x + 2y, x + y min
    # thì x + y min khi x >= y, nếu N chia hết cho 3 thì trả về N / 3 luôn, còn không thì trả về N / 3 + 1
    def minOperations(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        res = 0
        for i in dic:
            if dic[i] % 3 == 0:
                res += dic[i] // 3
            else:
                res += dic[i] // 3 + 1
        return res
