class Solution:
    # Chọn 1 i sao cho bên phải i có ít nhất 1 kí tự giống s[i], bên trái i có ít nhất 1 kí tự giống s[i], xóa cả 2
    # Như vậy để có được xâu có độ dài nhỏ nhất thì không cần để ý đến thứ tự các kí tự trong xâu mà chỉ cần quan tâm đến số lần xuất hiện mỗi kí tự
    # VỚi những kí tự xuất hiện lẻ lần thì ta xóa hết cho đến khi còn 1 kí tự, những kí tự xuất hiện chắn lần thì ta xóa hết cho đến khi còn 2 kí tự
    # Như vậy bài toán trở thành việc đếm số lần xuất hiện của mỗi kí tự trong xâu, nếu kí tự xuất hiện chẵn lần thì +2 vào kết quả, nếu kí tự xuất hiện lẻ lần thì +1 vào kết quả
    def minimumLength(self, s: str) -> int:
        d = Counter(s)
        res = 0
        for char, cnt in d.items():
            if cnt % 2 == 1:
                res += 1
            else:
                res += 2
        return res
