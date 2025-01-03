class Solution:
    # Mô tả đề đã khá rõ rồi, chỉ cần cộng dồn và so sánh
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        pre = 0
        s = sum(nums)
        for i in range(0, len(nums) - 1):
            pre += nums[i]
            if pre >= s - pre:
                res += 1
        return res
