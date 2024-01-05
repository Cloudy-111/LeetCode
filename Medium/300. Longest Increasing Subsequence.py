class Solution:
    # Cách 1: T = O(n^2). Với mỗi số trong nums, tìm số nào lớn nhất trước nó mà nhỏ hơn nó, cộng vị trí lên 1
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
        return res + 1

    # Cách 2: T = O(n log n), S = O(n)
    # tạo mảng tails có độ dài bằng với độ dài nums, có nhiệm vụ lưu trữ dãy con tăng dần
    # với mỗi lần duyệt qua 1 số trong nums, ta sẽ xác định vị trí của nó trong tails bằng Binary Search
    # vì tails chứa dãy con tăng dần nên độ phức tạp tg qua mỗi lần duyệt là O(log n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * (len(nums))
        size = 0  # kích cỡ dãy con tăng dần
        for num in nums:
            i, j = 0, size  # giống như left với right ý
            while i != j:
                mid = (i + j) // 2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            # khi tìm được i thì num sẽ thay thế vào vị trí i của tails
            tails[i] = num
            size = max(size, i + 1)
        return size
