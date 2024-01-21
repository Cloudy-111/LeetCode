class Solution:
    # Quy hoạch động, không lấy những nhà cạnh nhau nên tạo mảng phụ t có độ dài = nums
    # t có nhiệm vụ lưu trữ kết quả là số tiền lấy được khi đến nhà i
    # t[i] là số tiền lớn nhất lấy được khi đến nhà i = số tiền lớn nhất lấy được khi đến nhà i - 2 + số tiền nhà i
    # t[i] = max(t[:i - 2]) + nums[i]
    # kết quả chỉ cần so sánh t[-1] và t[-2]
    # T = O(n)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[1], nums[0])
        elif n == 3:
            return max(nums[1], nums[0] + nums[2])
        else:
            t = [0] * n
            t[0] = nums[0]
            t[1] = nums[1]
            m = t[0]
            for i in range(2, n):
                t[i] = m + nums[i]
                if t[i - 1] > m:
                    m = t[i - 1]
            return max(t[-1], t[-2])
