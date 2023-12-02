class Solution:  # Cửa số trượt với kích thước không cố định
    # chú ý, số lượng số 0 lớn nhất trong 1 cửa sổ là k
    # xét các cửa sổ có số lượng số 0 <= k
    # nếu đến cửa sổ có nhiều hơn k thì loại bỏ ở đầu
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:  # có nghĩa là đã xét hết k(hết cửa sổ), cần loại bỏ đầu
                if nums[left] == 0:
                    k += 1  # tức là hồi lại được 1 lần k ở left
                left += 1  # dịch bên trái đi 1
        return right - left + 1
