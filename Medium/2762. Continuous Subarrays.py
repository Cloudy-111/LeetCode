class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        left = right = 0
        freq = {}
        while right < len(nums):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            res += right - left + 1
            right += 1
        return res
