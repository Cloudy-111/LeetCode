class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        dic = Counter(nums)
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            # để kiểm tra xem dãy có tăng dần liên tiếp 1 đơn vị hay không
            if nums[i] - 1 == prefix[-1] and i == len(prefix):
                prefix.append(nums[i])
        res = sum(prefix)
        while dic[res] != 0:  # tìm kết quả nhỏ nhất
            res += 1
        return res
