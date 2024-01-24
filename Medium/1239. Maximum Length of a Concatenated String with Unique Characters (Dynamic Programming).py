class Solution:
    # Cách 1: Quay lui sinh nhị phân, xét tất cả tỏ hợp có thể có rồi tìm tổ hợp thoả mãn
    # T = n * 2^n -> Quá lâu, chưa tối ưu
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0

        def check(arr, mark):
            t = ''
            for i in range(len(arr)):
                if mark[i] == 1:
                    t += arr[i]
            if len(set(t)) == len(t):
                self.res = max(self.res, len(t))

        def bitGen(mark, i):
            for j in range(0, 2):
                mark[i] = j
                if i == len(mark) - 1:
                    check(arr, mark)
                else:
                    bitGen(mark, i + 1)
        mark = [0] * len(arr)
        bitGen(mark, 0)
        return self.res

    # Cách 2: nhận thấy chỉ cần tạo ra xâu s dài nhất mà không bị trùng lặp kí tự,
    # -> lưu những xâu không trùng lặp vào 1 mảng rồi duyệt qua mảng đó, cộng thêm những xâu được tạo mới từ xâu đã có và xâu từ mảng ban đầu
    # là 1 kiểu QUY HOẠCH ĐỘNG, lấy xâu nhỏ để tạo xâu lớn hơn
    # từ mỗi 1 xâu trong mảng ban đầu, tạo thêm được những xâu không trùng lặp mới bằng cách cộng thêm với xâu không trùng lặp đã có
    def maxLength(self, arr: List[str]) -> int:
        unique = ['']  # mảng gồm những xâu không trùng lặp kí tự
        res = 0
        for i in range(len(arr)):  # duyệt mảng ban đầu để tạo xâu
            curr = unique
            for j in range(len(curr)):  # duyệt qua mảng gồm các xâu không trùng lặp
                # kết hợp với xâu của mảng đầu xem có thỏa mãn hay không
                new = arr[i] + curr[j]
                if len(set(new)) == len(new):
                    unique.append(new)  # thỏa mãn thì thêm vào mảng
                    res = max(res, len(new))
        return res
