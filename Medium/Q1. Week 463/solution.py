class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        res = 0
        n = len(prices)
        for i in range(n):
            res += prices[i] * strategy[i]

        prefixBase = [0] * (n + 1)
        prefixPrice = [0] * (n + 1)

        for i in range(n):
            prefixBase[i + 1] = prefixBase[i] + prices[i] * strategy[i]
            prefixPrice[i + 1] = prefixPrice[i] + prices[i]

        maxDiff = 0
        for left in range(n - k + 1):
            right = left + k

            oldProfit = prefixBase[right] - prefixBase[left]
            newProfit = prefixPrice[right] - prefixPrice[left + k // 2]

            maxDiff = max(maxDiff, newProfit - oldProfit)

        return res + maxDiff
