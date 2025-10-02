class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            res += 1
            emptyBottles -= numExchange - 1
            numExchange += 1

        return res
