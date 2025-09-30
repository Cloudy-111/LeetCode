public class Solution {
    public int TriangularSum(int[] nums) {
        if (nums.Length == 1) return nums[0];
        if (nums.Length == 2) return (nums[0] + nums[1]) % 10;

        int n = nums.Length - 1;
        BigInteger pascal = 1;

        BigInteger res = nums[0] + nums[n];
        for(int i = 1; i < n; i++){
            pascal = pascal * (n - i + 1) / i;
            res += pascal * nums[i];
        }
        return (int)(res % 10);
    }
}
