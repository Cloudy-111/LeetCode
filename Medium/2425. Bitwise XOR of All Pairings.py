class Solution:
    # Mỗi phần tử của mảng nums1 kết hợp với 1 phần tử mảng nums2 -> số lần xuất hiện 1 phần tử của mảng nums1 là độ dài mảng nums2, và ngược lại
    # Khi XOR hết tất cả các cặp thỏa mãn thì ta chỉ quan tâm đến số lần xuất hiện mỗi phần tử
    # VÌ a XOR a = 0, a XOR 0 = a -> với phần tử xuất hiện lẻ lần thì vẫn giữ nguyên giá trị, còn phần tử xuất hiện chẵn lần thì giá trị sẽ bằng 0
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums1) % 2 == 1:
            for i in nums2:
                res ^= i
        if len(nums2) % 2 == 1:
            for i in nums1:
                res ^= i
        return res
