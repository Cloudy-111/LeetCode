class Solution:  # O(n) time complexity
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == res:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                res = nums[i]
                cnt = 1
        return res
    # có thể làm được như này vì số cần tìm là số xuất hiện nhiều hơn n / 2 lần với n = len(nums)
