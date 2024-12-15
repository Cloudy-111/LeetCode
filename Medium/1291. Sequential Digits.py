class Solution:
    # Cách 1: Tạo ra mảng chỉ gồm các số thỏa mãn, sau đó dùng 2 con trỏ để lấy được mảng cần tìm
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def gen(a):
            s = ''
            for i in range(1, a + 1):
                s = s + str(i)
            res = [int(s)]
            for i in range(a, 9):
                res.append(res[-1] + int('1' * a))
            return res
        l = len(str(low))
        r = len(str(high))
        res = []
        for i in range(l, r + 1):
            res += gen(i)
        l = 0
        r = len(res) - 1
        while l <= r:
            if res[l] >= low and res[r] <= high:
                return res[l: r + 1]
            if res[l] < low:
                l += 1
            if res[r] > high:
                r -= 1
        return []

    # Cách 2: Duyệt tất cả các cặp i, j(i < j) để cắt xâu '123456789', thỏa mãn low <= X <= high
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        t = '123456789'
        l = []
        for i in range(len(t)):
            for j in range(i+1, len(t)+1):
                if low <= int(t[i:j]) <= high:
                    l.append(int(t[i:j]))
        return sorted(l)
