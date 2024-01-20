class Solution:
    # Cách 1: dùng MonotonicStack, ở đầy là Stack mà chỉ có các phần tử tăng dần.
    # với mỗi lần duyệt tạo Stack thì là O(n)
    # như vậy, cả bài sẽ là O(n^2) --> chưa tối ưu
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7

        def monotonicStack(arr):
            stk = []
            res = 0
            for i in range(len(arr)):
                while len(stk) > 0 and arr[i] < stk[-1]:
                    stk.pop()
                stk.append(arr[i])
                res += stk[0]
            return res

        # giảm thời gian chạy đi 1 ít từ việc bỏ stack
        def monotonicStack(arr):
            res = arr[0]
            t = arr[0]
            for i in range(1, len(arr)):
                if arr[i] < t:
                    t = arr[i]
                res += t
            return res
        res = 0
        for i in range(len(arr)):
            res = (res + monotonicStack(arr[i:]) % mod) % mod
        return res

    # Cách 2: O(n), Với mỗi số trong mảng, tìm vị trí phần tử đầu tiên mà nhỏ hơn nó về phía bên phải và bên trái (left[i] và right[i]) (Sử dụng Monotonic Stack)
    # ta thấy, với left[i] và right[i] là 2 vị trí đầu tiên mà nhỏ hơn phtu đó, --> mảng con được tạo bởi left[i] và right[i] nhận phtu đó là nhỏ nhất
    # như vậy với mỗi số, số mảng con mà số đó là nhỏ nhất là (i - left[i]) * (right[i] - i)
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        left = [-1] * len(arr)
        right = [len(arr)] * len(arr)

        # sử dụng monotonicStack để tìm các vị trí, là giai đoạn tiền xử lí
        stack = []
        for idx, val in enumerate(arr):
            while stack and val < arr[stack[-1]]:
                stack.pop()
            if len(stack) != 0:
                left[idx] = stack[-1]
            stack.append(idx)
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if len(stack) != 0:
                right[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(len(arr)):
            res = (res + arr[i] * (i - left[i]) * (right[i] - i) % mod) % mod
        return res

    # Cách 3: O(n), rút gọn cách làm trên, theo hướng quy hoạch động
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Ví dụ: [3, 1, 2, 5, 4]
        # [3] -> 3
        # [3,1] [1] -> 1 + 1 = 2
        # [3,1,2] [1,2] [2] -> 2 + 2 = 4
        # [3,1,2,5] [1,2,5] [2,5] [5] -> 4 + 5 = 9
        # [3,1,2,5,4] [1,2,5,4] [2,5,4] [5,4] [4] -> 4 + 4 * 2 = 12

        arr = [0] + arr
        stack = [0]
        ans = [0] * len(arr)
        # mảng ans với ans[i] là tổng các phần tử nhỏ nhất trong các mảng con được tạo ra từ đầu cho đến i

        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            # j là vị trí đầu tiên nhỏ hơn phtu đang xét -> mảng con từ j đến i nhận phtu thứ i là nhỏ nhất
            j = stack[-1]
            # số lượng mảng con xét đến i = số lượng mảng con xét đến j + số lượng mảng con từ j đến i
            # -> kết quả tại i = kết quả tại j + (i - j) * arr[i]
            ans[i] = ans[j] + (i-j)*arr[i]
            stack.append(i)

        return sum(ans) % (10**9 + 7)
