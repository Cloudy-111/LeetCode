class Solution:
    # Đề là chia mảng thành 3 phần sao cho tổng các số bắt đầu mỗi mảng là nhỏ nhất
    # -> luôn chọn phtu đầu tiên của mảng, còn 2 phtu nữa
    # -> chọn 2 phtu nhỏ nhất của  mảng[1:]
    # T = O(n), dùng 2 biến  để theo dõi phtu nhỏ nhất
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        m1, m2 = 100, 100
        for i in range(1, n):
            if nums[i] < m1:
                m2 = m1
                m1 = nums[i]
            elif nums[i] < m2:
                m2 = nums[i]
        return nums[0] + m1 + m2
