class Solution:
    def totalMoney(self, n: int) -> int:
        last = n % 7
        weeks = n // 7
        return 28 * weeks + 7 * (weeks - 1) * weeks // 2 + (last + 1) * last // 2 + weeks * last
