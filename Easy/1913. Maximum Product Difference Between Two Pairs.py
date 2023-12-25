class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Cách 1 thì đơn giản rồi, trực quan nhất, sort mảng lại rôì lấy tích 2 số cuối trừ tích 2 số đầu
        # T: O(nlogn)
        # Cách 2 là duyệt O(n) với 4 biến min max tương ứng
        max1, max2 = 0, 0
        min1, min2 = 10000, 10000
        for i in range(len(nums)):
            if nums[i] > max1 and nums[i] > max2:
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max2 = nums[i]
        for i in range(len(nums)):
            if nums[i] < min1 and nums[i] < min2:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        return max1 * max2 - min1 * min2
