class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        res = 0
        while numBottles > 0:
            emptyBottles += numBottles
            res += numBottles
            numBottles = 0
            if emptyBottles >= numExchange:
                temp = 2 * emptyBottles + numExchange * (numExchange - 1)
                i = numExchange + 1
                while i * (i + 1) <= temp:
                    i += 1
                i -= 1
                # can replace calculate i by: i = (sqrt(1 + 4 * temp) - 1) // 2
                numBottles += i - numExchange + 1
                emptyBottles -= (i + numExchange) * (i - numExchange + 1) // 2
                numExchange = i + 1
        return res
