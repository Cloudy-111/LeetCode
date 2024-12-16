import heapq
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        res = 0
        pq = [-x for x in gifts]
        heapq.heapify(pq)

        while k > 0:
            tmp = heapq.heappop(pq)
            tmp = -tmp

            tmp = int(math.sqrt(tmp))
            heapq.heappush(pq, -tmp)
            k -= 1

        return -1 * sum(pq)
