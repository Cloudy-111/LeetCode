class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if b == d == f:  # Nếu 3 con cùng 1 hàng ngang
            print(1)
            if (c - a) * (c - e) < 0:  # nếu con tượng ở giữa
                return 2
            else:
                return 1
        elif a == c == e:  # nếu 3 con cùng 1 hàng dọc
            print(2)
            if (d - b) * (d - f) < 0:  # nếu con tượng ở giữa
                return 2
            else:
                return 1
        # nếu 3 con cùng 1 đùng chéo
        elif abs(a - c) == abs(b - d) and abs(a - e) == abs(b - f) and abs(c - e) == abs(d - f):
            print(3)
            if (a - c) * (a - e) < 0 and (b - d) * (b - f) < 0:  # nếu con xe ở giữa
                return 2
            else:
                return 1
        # nếu xe không thẳng hậu và tượng cũng không thẳng hậu
        elif a != e and b != f and abs(c - e) != abs(d - f):
            print(4)
            return 2
        else:  # các trường hợp còn lại
            print(5)
            return 1
