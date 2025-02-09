from typing import Counter

# tìm số lượng cặp i < j và j - i != nums[j] - nums[i]
# tương đương với tìm số lượng cặp i < j và j - i == nums[j] - nums[i] và lấy tổng lượng cặp i < j trừ đi nó
# j - i == nums[j] - nums[i] tương đương với nums[j] - j == nums[i] - i
# vậy ta sẽ tạo mảng arr với arr[i] = nums[i] - i và đếm những kết quả bằng nhau trong nó trong 1 dict
# Cứ 2 kết quả bằng nhau, tạo được 1 cặp thỏa mãn => kC2 với k là số lượng kết quả bằng nhau với mỗi kết quả
# return tổng số cặp có thể tạo - số cặp good đã tạo được


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        arr = []
        n = len(nums)
        for idx, num in enumerate(nums):
            arr.append(num - idx)
        d = Counter(arr)
        number_of_good_pairs = 0
        total_pair = (n * (n - 1)) // 2
        for key, values in d.items():
            number_of_good_pairs += (values * (values - 1)) // 2
        return total_pair - number_of_good_pairs
