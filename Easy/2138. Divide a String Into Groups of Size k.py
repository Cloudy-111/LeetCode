class Solution:
    # đề là chia thành các nhóm có độ dài k, không  thay đôri vị trí kí tự, nếu không đủ k kí tự thì fill vào
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            res.append(s[i: i + k])
        if len(res[-1]) < k:
            res[-1] += (k - len(res[-1])) * fill
        return res
