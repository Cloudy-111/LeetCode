public class Solution {
    public int MaximumDifference(int[] nums) {
        int res = 0;
        int max_value = nums[nums.Length - 1];

        for(int i = nums.Length - 2; i >= 0; i--) {
            if (nums[i] < max_value) {
                res = Math.Max(res, max_value - nums[i]);
            } else {
                max_value = Math.Max(max_value, nums[i]);
            }
        }
        return res > 0 ? res : -1;
    }
}