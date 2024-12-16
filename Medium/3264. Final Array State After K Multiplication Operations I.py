import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(pq)
        while k:
            _, idx = heapq.heappop(pq)
            nums[idx] *= multiplier
            heapq.heappush(pq, (nums[idx], idx))
            k -= 1
        return nums
