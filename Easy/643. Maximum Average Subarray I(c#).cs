public class Solution
{
    public double FindMaxAverage(int[] nums, int k)
    {
        double tmp = 0;
        for (int i = 0; i < k; i++) tmp += nums[i] * 1.0;
        double res = tmp / k;
        for (int i = k; i < nums.Length; i++)
        {
            tmp -= nums[i - k];
            tmp += nums[i];
            res = Math.Max(res, tmp / k);
        }
        return res;

    }
}