class Solution:
    # đối xứng thì trả về 1, còn không  thì trả về 2
    # phân biệt giữa xâu con và đoạn con
    # xâu con là xâu được tạo ra từ xâu ban đầu bớt đi 1 vài kí tự hoặc không, không cần liên tiếp
    # đoạn con thì phải liên tiếp
    # vậy bài này chỉ cần kiểm tra xem s có đối xứng hay không, nếu đối xứng thì trả về 1, còn không thì trả về 2 (vì chỉ có 2 kí tự là a, b)
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2
