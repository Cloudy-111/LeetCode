class Solution:
    # là bài tìm độ dài dãy toàn số 1 dài nhất sau khi thay thế 0 thành 1 với số lần là k(với bài này k = 1)
    # 1004. Max Consecutive Ones III
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        left, right = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left
