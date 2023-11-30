class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False

        min_val = float('inf')
        second = float('inf')

        for num in nums:
            if num <= min_val:
                min_val = num
            elif num <= second:
                second = num
            else:
                return True

        return False
