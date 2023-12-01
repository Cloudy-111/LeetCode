class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                cnt += 1
            else:
                zeros += 1
        for i in range(zeros):
            nums[-1 - i] = 0
