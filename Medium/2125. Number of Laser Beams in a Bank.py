class Solution:
    # đề đọc hơi dài thôi mà cũng dễ, chỉ cần tỉnh tổng các tích của 2 hàng liên tiếp có số 1, mà độ phức tạp là O(n^2)
    def numberOfBeams(self, bank: List[str]) -> int:
        lst = []
        for i in bank:
            cnt = i.count('1')
            if cnt > 0:
                lst.append(cnt)
        res = 0
        for i in range(1, len(lst)):
            res += lst[i] * lst[i - 1]
        return res
