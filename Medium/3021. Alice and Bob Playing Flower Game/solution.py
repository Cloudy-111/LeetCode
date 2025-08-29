class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        num_of_odd_in_n = (n - 1) // 2 + 1
        num_of_even_in_m = (m - 2) // 2 + 1 if m > 1 else 0
        return (num_of_odd_in_n * num_of_even_in_m) + (n - num_of_odd_in_n) * (m - num_of_even_in_m)
