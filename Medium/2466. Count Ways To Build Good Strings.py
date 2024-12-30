class Solution:
    # Dùng quy hoạch động để giải quyết
    # Phân tích đề bài, nhận thấy những xâu có độ dài A được tạo ra bởi xâu có độ dài A - zero hoặc A - one bằng cách thêm số lượng zero hoặc one vào xâu
    # Vì vậy ta sẽ tạo ra một mảng dp với dp[i] là số lượng xâu có độ dài i
    # dp[i] += dp[i - zero] + dp[i - one]
    # dp[zero] = 1, dp[one] = 1 có nghĩa là có 1 xâu có độ dài zero và 1 xâu có độ dài one
    # nếu zero == one thì dp[zero] = 2
    # với dp[1] thì sẽ là số lượng xâu có độ dài 1 có số lượng zero hoặc one bằng 1
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        M = 10**9 + 7
        dp = [0] * (high + 1)
        dp[zero] = 1
        dp[one] = 1
        if zero == one:
            dp[zero] = 2
        dp[1] = (zero == 1 if 1 else 0) + (one == 1 if 1 else 0)
        for i in range(2, high + 1):
            dp[i] += (dp[i - zero] + dp[i - one]) % M
        res = 0
        for i in range(low, high + 1):
            res += dp[i] % M
        return res % M
