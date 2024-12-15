class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        i = (n - 1) // 2 + 1
        j = (m - 2) // 2 + 1 if m > 1 else 0
        return i * j + (n - i) * (m - j)
