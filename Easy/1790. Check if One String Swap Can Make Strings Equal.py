class Solution:
    # Đề bai yêu cầu tìm xem xâu có thể swap 2 vị trí nhiều nhất 1 lần được hay không
    # Biến cnt để lưu số lượng vị tri khác nhau giữa 2 xâu
    # Biến d1 và d2 để lưu các kí tự khác nhau giữa 2 xâu
    # Nếu cnt = 0 tức là 2 xâu giống nhau, return True
    # Nếu cnt = 2, return d1 == d2
    # Còn lại return False
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        d1 = ""
        d2 = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                d1 += s1[i]
                d2 = s2[i] + d2
        if cnt == 0:
            return True
        if cnt == 2:
            return d1 == d2
        return False
