class Solution:
    # Ý tưởng: Dùng quy hoạch động để giải quyết bài toán
    # Với bài toán tìm 3 mảng con không giao nhau mà có tổng lớn nhất thì ta tìm mảng con có tổng lớn nhất bên trái
    # Sau đó tìm mảng con có tổng lớn nhất bên phải, và cuối cùng là mảng con có tổng lớn nhất ở giữa
    # Vì đề bài yêu cầu mảng con có độ dài là k nên ta sẽ tính tổng của các mảng con có độ dài k
    # Tính tổng của các mảng con có độ dài k bằng cách tính tổng của các phần tử từ i đến i + k, áp dụng prefixSum để không phải tính sum nhiều lần
    # Tìm mảng con có tổng lớn nhất bên trái: duyệt qua mảng prefixSum, nếu prefixSum[i] > max_sum thì cập nhật max_sum và idx = i
    # Tìm mảng con có tổng lớn nhất bên phải: duyệt qua mảng prefixSum từ phải sang trái, nếu prefixSum[i] >= max_sum thì cập nhật max_sum và idx = i
    # Tìm mảng con có tổng lớn nhất ở giữa: duyệt qua mảng prefixSum, tính tổng của 3 mảng con và so sánh với max_sum để cập nhật kết quả
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefixSum = [0] * (n - k + 1)
        arr = [0] * (n + 1)
        for i in range(1, n + 1):
            arr[i] = arr[i - 1] + nums[i - 1]
        for i in range(n - k + 1):
            prefixSum[i] = arr[i + k] - arr[i]

        # Mảng left lưu vị trí của mảng con có tổng lớn nhất bên trái
        left = [0] * (n - k + 1)
        idx = 0
        max_sum = 0
        for i in range(n - k + 1):
            if prefixSum[i] > max_sum:
                max_sum = prefixSum[i]
                idx = i
            left[i] = idx

        # Mảng right lưu vị trí của mảng con có tổng lớn nhất bên phải
        right = [0] * (n - k + 1)
        idx = n - k
        max_sum = 0
        for i in range(n - k, -1, -1):
            if prefixSum[i] >= max_sum:
                max_sum = prefixSum[i]
                idx = i
            right[i] = idx

        max_sum = 0
        res = [-1, -1, -1]
        # Duyệt qua các mảng con ở giữa để tìm ra tổng 3 mảng con lớn nhất
        for i in range(k, len(prefixSum) - k):
            l, r = left[i - k], right[i + k]
            total = prefixSum[i] + prefixSum[l] + prefixSum[r]
            if total > max_sum:
                max_sum = total
                res = [l, i, r]
        return res
