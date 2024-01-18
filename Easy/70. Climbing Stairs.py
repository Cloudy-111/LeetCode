class Solution:
    # khi bước từ bậc n đến bậc n + 1 ta có 2 cách bước: bước 1 bậc từ bậc n hoặc bước 2 bậc từ bậc n - 1
    # như vậy số cách bước đến bậc n + 1 = số cách bước đến bậc n + số cách bước đến bậc n - 1
    # F(n + 1) = F(n) + F(n - 1)
    # 1 dạng của quy hoạch động
    def climbStairs(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1
        for i in range(2, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]
