from bisect import *


class Solution:
    # Cách 1(Trực quan nhất): tạo dict cho mảng rồi tìm xem số nào xuất hiện nhiều hơn len(arr) / 4 lần là được
    # Time, Space complexity: O(n)
    # có thể dùng dict rỗng rồi cộng dần từng phần tử, phần tử nào có số lần xuất hiện nhiều hơn len(arr) / 4 thì trả về phần tử đó
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = Counter(arr)
        for i in dic:
            if dic[i] > len(arr) / 4:
                return i
    # Cách 2: từ dữ liệu đề bài: mảng đã sắp xếp không giảm, có số mà số lần xuất hiện > 25%
    # -> chỉ cần xét theo khối có độ dài là len(arr) / 4, nếu phtu đầu và cuối giống nhau thì trả về phtu đó
    # Time complexity: O(n), Space complexity: O(1)

    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr) // 4
        for i in range(len(arr) - size):
            if arr[i] == arr[i + size]:
                return arr[i]
    # Cách 3: từ dữ liệu đề cho: mảng đã sấp xếp -> suy nghĩ đến Binary Search
    # Time complexity: O(logn), Space complexity: O(1)
    # số cần tìm có số lần xuất hiện > 25% -> chia dãy số ban đầu làm 3: len(arr) // 4, len(arr) // 2, 3 * len(arr) // 4
    # như vậy block có số cần tìm sẽ phải lượt qua ít nhất 1 số trong 3 vị trí trên
    # -> với mỗi số, tìm độ dài của block số đó, nếu > 25% thì return nó

    def findSpecialInteger(self, arr: List[int]) -> int:
        index = [arr[len(arr) // 4], arr[len(arr) // 2],
                 arr[3 * len(arr) // 4]]
        for num in index:
            # bisect_left để tìm kiếm vị trí và có thể thêm vào bên trái số đó mà không thay đổi thứ tự ban đầu của dãy
            left = bisect_left(arr, num)
            right = bisect_right(arr, num) - 1
            if right - left + 1 > len(arr) // 4:  # độ dài block
                return num
