class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(61):
            temp = num1 - k * num2
            if temp <= 0:
                return -1
            if temp == 1 and k > 1:
                return -1
            num_operations = self.count_bit(temp)
            if num_operations <= k:
                return k
        return -1

    def count_bit(self, n):
        res = 0
        while n > 0:
            if n % 2 == 1:
                res += 1
            n >>= 1
        return res
