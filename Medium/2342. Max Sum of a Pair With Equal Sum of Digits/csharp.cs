public class Solution
{
    public int MaximumSum(int[] nums)
    {
        Dictionary<int, List<int>> sum_digit = new Dictionary<int, List<int>>();
        for (int i = 0; i < nums.Length; i++)
        {
            int tmp = sumDigit(nums[i]);
            if (!sum_digit.ContainsKey(tmp))
            {
                sum_digit[tmp] = new List<int> { nums[i], -1 };
            }
            else
            {
                if (nums[i] >= sum_digit[tmp][0])
                {
                    sum_digit[tmp][1] = sum_digit[tmp][0];
                    sum_digit[tmp][0] = nums[i];
                }
                else if (nums[i] > sum_digit[tmp][1])
                {
                    sum_digit[tmp][1] = nums[i];
                }
            }
        }
        int res = -1;
        foreach (var item in sum_digit)
        {
            if (item.Value[1] != -1)
            {
                res = Math.Max(res, item.Value[0] + item.Value[1]);
            }
        }
        return res;
    }
    private int sumDigit(int num)
    {
        int res = 0;
        while (num > 0)
        {
            res += num % 10;
            num /= 10;
        }
        return res;
    }
}