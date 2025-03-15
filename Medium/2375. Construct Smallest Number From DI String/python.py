class Solution:
    # Ta tạo một stack lưu các số sẽ được thêm vào xâu
    # số nhỏ nhất sẽ là 1, Khi gặp I hoặc đến cuối chuỗi thì lần lượt pop hết stack
    # Khi gặp D, ta giữ số trong stack để đảm bảo thứ tự giảm dần.
    # Như vậy thì số ở top stack luôn là số lớn nhất stack
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = ""
        start = 1
        for i, char in enumerate(pattern):
            stack.append(str(start))
            start += 1

            if char == 'I':
                while stack:
                    res += stack.pop()
        stack.append(str(start))
        while stack:
            res += stack.pop()
        return res
