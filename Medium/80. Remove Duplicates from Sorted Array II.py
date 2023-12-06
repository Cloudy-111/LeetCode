class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        nums[k] = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[k] and cnt < 2:
                k += 1
                nums[k] = nums[i]
                cnt += 1
            elif nums[i] != nums[k]:
                cnt = 1
                k += 1
                nums[k] = nums[i]
        return k + 1
