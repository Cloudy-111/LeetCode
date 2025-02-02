class Solution:
    # If the result returns False, there are only 2 cases: the sequence has 2 decreasing times or the first element is smaller than the last element.
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
        if cnt == 0: return True
        if cnt > 1: return False
        if nums[0] < nums[len(nums) - 1]: return False
        return True