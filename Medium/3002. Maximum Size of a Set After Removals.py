class Solution:
    # mỗi mảng lấy đi n / 2 phần tử có nghĩa là mỗi mảng còn n / 2 phần tử
    # để có được set dài nhất, ta cần phải lấy được những phần tử xuất hiện trong mảng này mà không xuất hiện trong mảng kia
    # hết những phần tử như vậy thì xét tiếp đến những phần tử trùng nhau
    # giới hạn lớn nhất của độ dài set là n
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        dic1 = {}
        dic2 = {}
        for i in nums1:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for i in nums2:
            if i in dic2:
                dic2[i] += 1
            else:
                dic2[i] = 1
        cnt1, cnt2 = 0, 0
        # tìm số lượng số chỉ xuất hiện trong mảng 1
        for i in dic1:
            if i not in dic2:
                cnt1 += 1
        # nếu số lượng đó còn lớn hơn độ dài mảng / 2 thì bỏ cho đến khi bằng
        if cnt1 > len(nums1) // 2:
            cnt1 = len(nums1) // 2
        # tìm số lượng số chỉ xuất hiện trong mảng 2
        for i in dic2:
            if i not in dic1:
                cnt2 += 1
        if cnt2 > len(nums1) // 2:
            cnt2 = len(nums1) // 2

        cnt3 = 0
        # tìm số xuất hiện trong cả 2 mảng
        for i in dic1:
            if i in dic2:
                cnt3 += 1
        res = cnt1 + cnt2 + cnt3
        # giới hạn lớn nhất là độ dài mảng(n)
        return res if res < len(nums1) else len(nums1)
