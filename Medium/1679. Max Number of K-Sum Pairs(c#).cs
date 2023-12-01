public class Solution
{
    public int MaxOperations(int[] nums, int k)
    {
        Array.Sort(nums);
        int l = 0, r = nums.Length - 1, res = 0;
        while (l < r)
        {
            int tmp = nums[l] + nums[r];
            if (tmp == k)
            {
                res++;
                l++;
                r--;
            }
            else if (tmp < k) l++;
            else r--;
        }
        return res;
    }
}