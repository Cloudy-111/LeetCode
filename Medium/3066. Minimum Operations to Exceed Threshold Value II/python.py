import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while len(nums) >= 2 and nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            heapq.heappush(nums, first * 2 + second)
            res += 1
        return res
