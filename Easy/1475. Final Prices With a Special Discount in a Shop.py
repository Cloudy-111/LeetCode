import heapq


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        arr = [0] * len(prices)
        for i in range(len(prices)):
            while len(st) and prices[i] <= prices[st[-1]]:
                arr[st.pop()] = i
            st.append(i)
        for i in range(len(prices)):
            if arr[i]:
                prices[i] -= arr[i]
        return prices
