class Solution:
    # dùng dict để kiểm soát vị trí bắt đầu và kết thúc của 1 kí tự, sau khi đã có đựợc rồi thì duyệt
    # nếu vị trí bắt đầu của 1 kí tự mà lớn hơn vị trí kết thúc của khoảng trước thì danh sach kết quả sẽ được thêm độ dài đoạn trước vào
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        s = s + '.'
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i, i]
            else:
                dic[s[i]][1] = i
        start = dic[s[0]]
        first = start[0]
        last = start[1]
        res = []
        for i in dic:
            tmp = dic[i]
            if tmp[0] > last:
                res.append(last - first + 1)
                first = tmp[0]
                last = tmp[1]
            else:
                last = max(last, tmp[1])
        return res
