class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = 0
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
            max_freq = max(max_freq, freq[i])
        res = 0
        for i in freq.values():
            if i == max_freq:
                res += i
        return res
