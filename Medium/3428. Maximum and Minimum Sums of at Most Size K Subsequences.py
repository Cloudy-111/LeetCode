class Solution:
    # https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/solutions/6302336/python-beat-100-hope-you-can-understand-oy60a/
    def minMaxSums(self, nums: List[int], k: int) -> int:
        n = len(nums)
        length = max(k, n)
        nums.sort()
        arr = [0] * length
        arr[0] = 1
        res = 0
        mod = 10**9 + 7
        for i in range(n):
            x = nums[i]
            y = nums[n - i - 1]
            # Iterate backwards from k to 1 to avoid overwriting the state
            for j in range(min(k, i), 0, -1):
                arr[j] += arr[j - 1]
            res += (sum(arr[:k]) % mod * ((x + y) % mod)) % mod
            # print(arr, sum(arr[:k]) * (x + y), x, y)
        return res % mod
