class Solution:
    # Theo dõi trạng thái xuất hiện của các phần tử
    # Số lượng phần tử đã xuất hiện ở cả 2 mảng từ đầu đến vị trí i =
    # Số lượng phần tử đã xuất hiện ở cả 2 mảng từ đầu đến vị trí i - 1 cộng với số lượng phần tử đã xuất hiện ở cả 2 mảng tại vị trí i
    # vì cả 2 mảng đều là hoán vị của các số từ 1 đến n nên mỗi số chỉ xuất hiện 1 lần trong mỗi mảng
    # res[-1] luôn lưu trữ số lượng phần tử chung đến chỉ mục hiện tại i - 1
    # Nếu A[i] == B[i]: Phần tử đó tự động là phần tử chung. Cập nhật res tăng lên 1 và đánh dấu arr[A[i]] = 1.
    # Nếu A[i] khác B[i]:
    # Xem xét xem các số A[i] và B[i] đã xuất hiện trong các đoạn trước không (dựa vào arr).
    # Cập nhật res với số lượng phần tử chung tính từ res[-1], đồng thời đánh dấu arr[A[i]] = 1 và arr[B[i]] = 1.
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        arr = [0] * (n + 1)
        res = [0]
        for i in range(len(A)):
            if A[i] == B[i]:
                res.append(res[-1] + 1)
                arr[A[i]] = 1
            else:
                res.append(arr[A[i]] + arr[B[i]] + res[-1])
                arr[A[i]] = 1
                arr[B[i]] = 1
        return res[1:]
