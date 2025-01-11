class Solution:
    # Để xác định xem xâu có thể tạo ra được k xâu đối xứng hay không thì nó phụ thuộc vào số lượng kí tự xuất hiện lẻ lần
    # Nếu số lượng kí tự xuất hiện lẻ lần lớn hơn k thì không thể tạo ra được k xâu đối xứng
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if k > len(s):
            return False
        counter = Counter(s)
        cnt = 0
        for char, count in counter.items():
            if count % 2 == 1:
                cnt += 1
        return k >= cnt
