class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        additional = numBottles
        while numBottles >= numExchange:
            res += additional
            additional = numBottles // numExchange
            emptyBottles = numBottles % numExchange
            numBottles = additional + emptyBottles
        return res + additional
