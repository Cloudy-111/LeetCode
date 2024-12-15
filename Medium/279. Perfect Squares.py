class Solution:
    # Quy hoạch động: F[n] = min(1 + F[n - A[j]])
    # với A[j] là phần tử thứ j trong mảng số cp A
    # F[n] là số lượng số cần dùng ít nhất để tính toán ra số n
    # 1 có nghĩa là thêm 1 số A[j] vào tổng trước đó để tạo thành số i
    # suy ra được giá trị trung gian F[i] = min(1 + F[i - A[j]]) với A[j] <= i

    def numSquares(self, n: int) -> int:
        t = int(sqrt(n))
        if t ** 2 == n:
            return 1
        arr = []
        i = 1
        while i * i <= n:
            arr.append(i * i)
            i += 1

        def solve(arr, n):
            res = [0] * (n + 1)
            for i in range(1, n + 1):
                tmp = float('inf')
                j = 0
                while j < len(arr) and arr[j] <= i:
                    tmp = min(tmp, 1 + res[i - arr[j]])
                    j += 1
                res[i] = tmp
            return res[n]
        return solve(arr, n)
