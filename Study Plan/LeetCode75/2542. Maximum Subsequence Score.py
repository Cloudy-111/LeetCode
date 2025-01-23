import heapq


class Solution:
    # Đề bài yêu cầu tìm tích lớn nhất giữa k số chọn trong nums1 với số nhỏ nhất trong k số chọn trong nums2, các số tương ứng vị trí với nhau
    # Có nghĩa là với mỗi số nhỏ nhất trong k số chọn trong nums2 thì sẽ có được k số có tổng lớn nhất trong nums1(với điều kiện vẫn tương ứng vị trí)
    # vì vậy đầu tiên ta sẽ sắp xếp mảng nums2 và nums1 theo thứ tự tăng dần của nums2(để giữ tính tương ứng)
    # Bởi vì chọn k số trong nums2 nên số lớn nhất trong các lần chọn số nhỏ nhất trong k số được chọn của nums2 sẽ ở vị trí n - k
    # Với việc chọn số ở vị trí n - k, ta sẽ có được tổng lớn nhất của k số được chọn trong nums1 sẽ là tổng của các số từ vị trí n - k đến n - 1
    # Duyệt từ n - k - 1 đến đầu nums2, ta sẽ lấy được số nhỏ nhất trong k số được chọn trong nums2 trong mỗi lần chọn
    # khi dịch giảm dần theo nums2, để giữ được tổng lớn nhất của k số được chọn trong nums1, ta sẽ sử dụng heapq để loại số nhỏ nhất ra khỏi tập k số được lấy
    # và thêm số mới vào, sau mỗi lần thêm số mới vào ta sẽ cập nhật lại tổng lớn nhất của k số được chọn trong nums1
    # https://leetcode.com/problems/maximum-subsequence-score/solutions/6320427/priority-queue-visual-example-and-explai-9fon/
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_indices = sorted(range(len(nums2)), key=lambda i: nums2[i])

        nums1_sorted = [nums1[i] for i in sorted_indices]
        nums2_sorted = [nums2[i] for i in sorted_indices]

        n = len(nums2)

        rest = nums1_sorted[n - k:]
        sum_rest = sum(rest)
        heapq.heapify(rest)
        res = nums2_sorted[n - k] * sum_rest
        for i in range(n - k - 1, -1, -1):
            sum_rest += nums1_sorted[i]
            sum_rest -= heapq.heappushpop(rest, nums1_sorted[i])
            res = max(res, nums2_sorted[i] * sum_rest)

        return res
