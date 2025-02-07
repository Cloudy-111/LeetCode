from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = defaultdict(int)  # Lưu màu của mỗi phần tử
        seen = defaultdict(int)  # Đếm số lần xuất hiện của mỗi màu
        tmp = 0  # Số lượng màu duy nhất
        res = []
        for ball, color in queries:
            prev_color = d[ball]
            if prev_color != color:
                if prev_color > 0:
                    seen[prev_color] -= 1
                    if seen[prev_color] == 0:
                        tmp -= 1  # Loại bỏ màu cũ nếu không còn phần tử nào có màu đó
                if seen[color] == 0:
                    tmp += 1  # Thêm màu mới nếu nó chưa có trước đó
                seen[color] += 1
            d[ball] = color  # Cập nhật màu mới cho ball
            res.append(tmp)
        return res
