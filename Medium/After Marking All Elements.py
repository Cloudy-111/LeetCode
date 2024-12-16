import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [0] * (len(nums) + 1)
        pq = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(pq)

        score = 0
        while pq:
            num, idx = heapq.heappop(pq)

            if marked[idx] == 0:
                score += num
                marked[idx] = 1
                marked[idx + 1] = 1
                if idx - 1 >= 0:
                    marked[idx - 1] = 1
        return score
