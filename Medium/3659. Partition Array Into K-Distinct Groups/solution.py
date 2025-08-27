class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        num_group = n // k
        d = dict()
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        for v in d.values():
            if v > num_group:
                return False
        return True
