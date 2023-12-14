class Solution:
    # chỉ cần tìm số nào lớn nhất trong string đó là được rồi
    # vì các số hạng chỉ được tạo từ 0 và 1
    def minPartitions(self, n: str) -> int:
        res = '0'
        for i in n:
            if i > res:
                res = i
        return int(res)
