from collections import defaultdict

# Đếm số lượng tích của mỗi phần tử với các phần tử còn lại, nếu tích đó xuất hiện >= 4 lần thì có tồn tại 4 số a,b,c,d thỏa mãn
# với mỗi bộ số thỏa mãn thì có 8 cặp tìm được


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        cnt = 0
        d = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    prod = nums[i] * nums[j]
                    if prod not in d:
                        d[prod] = 1
                    d[prod] += 1
                    if d[prod] >= 4 and d[prod] % 2 == 0:
                        cnt += d[prod] // 2 - 1
                        # print(prod)
        return cnt * 8

# Giảm số lần duyệt tích bằng cách chỉ duyệt từ i + 1 vì tích của a,b sẽ bằng tích của b,a
# Sử dụng defaultdict để không cần phải kiểm tra key có tồn tại hay không


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        cnt = 0
        d = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                cnt += d[prod]
                d[prod] += 1
        return cnt * 8
