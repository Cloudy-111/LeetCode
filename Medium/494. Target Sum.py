class Solution:
    # Ý tưởng đầu tiên: Dùng backtracking để thử tất cả các trường hợp của mảng nums với 2 trường hợp + và -.
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        s = sum(nums)
        if s < target or -s > target:
            return 0
        # if s == target or -s == target: return 1
        cnt = [0]
        arr = []
        self.backtrack(arr, nums, target, cnt)
        return cnt[0]

    def backtrack(self, arr, nums, target, cnt):
        # if len(arr) == len(nums): print(sum(arr), len(arr))
        if len(arr) == len(nums) and sum(arr) == target:
            cnt[0] += 1
            return
        if len(arr) < len(nums):
            for i in "+-":
                if i == "+":
                    tmp = nums[len(arr)]
                else:
                    tmp = -nums[len(arr)]
                arr.append(tmp)
                self.backtrack(arr, nums, target, cnt)
                arr.pop()

# Dùng quy hoạch động để giải quyết:
# Có: Tổng số được gán dấu +  cộng với tổng số được gán dấu trừ là tổng của mảng nums.
# Tổng số được gán dấu + trừ đi tổng số được gán dấu trừ bằng target
# => Tổng số được gán dấu + bằng (target + sum(nums)) // 2
# Như vậy bài toán chỉ còn là tìm số cách chọn các số được gán dấu + sao cho tổng của chúng bằng (target + sum(nums)) // 2


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if (target + s) % 2 == 1 or target > s or target < -s:
            return 0
        P = (target + s) // 2
        dp = [0] * (P + 1)
        dp[0] = 1  # chỉ có 1 cách chọn mà không có số được gán dấu + nào
        for num in nums:
            # duyệt ngược để không ghi đè giá trị đã được cập nhật
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[P]
