class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0]
        for i in nums:
            pre.append(pre[-1] + i)
        leftSum = 0
        rightSum = pre[-1]
        ans = -1
        for i in range(len(nums)):
            if i > 0:
                leftSum += nums[i - 1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                ans = i
                break
        return ans
