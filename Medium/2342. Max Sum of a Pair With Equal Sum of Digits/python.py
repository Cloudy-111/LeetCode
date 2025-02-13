class Solution:
    # Với mỗi tổng các kí tự tìm được, ta lấy 2 số lớn nhất và cộng lại với nhau và trả về kết quả
    # Ý tưởng đầug tiên thì dùng heapq để lấy 2 số lớn nhất, nhưng vì chỉ cần 2 số lớn nhất nên ta có thể dùng 2 biến để lưu 2 số lớn nhất là được
    def maximumSum(self, nums: List[int]) -> int:
        def sumDigit(num):
            s = 0
            while num > 0:
                s += num % 10
                num = num // 10
            return s
        sum_digit = {}
        for i in nums:
            s = sumDigit(i)
            if s not in sum_digit:
                sum_digit[s] = [i, -1]
            else:
                if i >= sum_digit[s][0]:
                    sum_digit[s][0], sum_digit[s][1] = i, sum_digit[s][0]
                elif i > sum_digit[s][1]:
                    sum_digit[s][1] = i
        res = -1
        for key in sum_digit:
            if sum_digit[key][1] != -1:
                res = max(res, sum_digit[key][0] + sum_digit[key][1])
        return res
