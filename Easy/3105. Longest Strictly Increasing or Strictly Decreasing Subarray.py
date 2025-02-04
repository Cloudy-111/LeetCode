class Solution:
    # duyệt 1 lần tìm độ dài dãy tăng dài nhất, duyệt lần 2 tìm độ dài dãy giảm dài nhất
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        tmp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                tmp += 1
            else:
                tmp = 1
            res = max(res, tmp)
        tmp = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                tmp += 1
            else:
                tmp = 1
            res = max(res, tmp)
        return res

    # hoặc có thể duyệt 1 lần trong 1 vòng lặp
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            res = max(res, inc, dec)
        return res
