class Solution:  # làm với O(n) và không sử dụng phép chia
    # tạo mảng pre và suff để hiểu hơn
    # VD dãy 1 2 3 4
    # 1 2 3 4
    # pre : x  1  2 6
    # suff: 24 12 4 x
    # x coi là 1
    # kết quả sẽ là pre[i] * suff[i]
    # bài dưới rút gọn được 1 bước là tạo mảng suff, kết hợp luôn với tính suffix
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        tmp = 1
        for i in range(len(nums) - 1):
            tmp *= i
            pre.append(tmp)
        tmp = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            pre[i] *= tmp
            tmp *= nums[i]
        return pre
