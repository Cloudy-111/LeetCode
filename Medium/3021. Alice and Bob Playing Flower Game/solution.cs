public class Solution {
    public long FlowerGame(int n, int m) {
        long num_odd_in_n = (n - 1) / 2 + 1;
        long num_even_in_m = m > 1 ? (m - 2) / 2 + 1 : 0;
        return num_odd_in_n * num_even_in_m + (n - num_odd_in_n) * (m - num_even_in_m);
    }
}