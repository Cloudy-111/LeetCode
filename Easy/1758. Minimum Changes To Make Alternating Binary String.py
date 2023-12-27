class Solution:
    # Cách 1: nhìn như nào thì hiểu như vậy, trâu
    # tạo lst bắt đầu là 1 với là 0 rồi so sánh dần với từng kí tự trong chuỗi, lấy kết quả nhỏ hơn trong 2 lần
    def minOperations(self, s: str) -> int:
        lst = [1]
        m1, m2 = 0, 0
        if s[0] != '1':
            m1 += 1
        if s[0] != '0':
            m2 += 1
        for i in range(1, len(s)):
            x = int(s[i])
            if lst[-1] == x:
                m1 += 1
                lst.append(abs(x - 1))
            else:
                lst.append(x)
        lstt = [0]
        for i in range(1, len(s)):
            x = int(s[i])
            if lstt[-1] == x:
                m1 += 1
                lstt.append(abs(x - 1))
            else:
                lstt.append(x)
        return min(m1, m2)

    # Cách 2: Để ý thấy xâu cần tạo có dạng là 010101... hoặc 101010...
    # vậy tách ra thành 2 xâu, một xâu gồm những kí tự ở vị trí lẻ, 1 xâu gồm những kí tự ở vị trí chắn
    # thì 2 xâu thu được sẽ có dạng 0000... và 11111...
    # như vậy, từ xâu ban đầu, tách thành 2 xâu, 1 xâu đếm số lượng số 1(tức là số lượng số cần chuyển đổi), xâu còn lại đếm số lượng số 0 và ngược lại
    # so sánh 2 tổng đó rồi lấy min được kết quả
    def minOperations(self, s: str) -> int:
        s1 = s[::2]
        s2 = s[1::2]
        s1_1 = s1.count('1')
        s2_0 = s2.count('0')
        return min(s1_1 + s2_0, len(s1) - s1_1 + len(s2) - s2_0)
