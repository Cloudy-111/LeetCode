public class Solution
{
    public long CountBadPairs(int[] nums)
    {
        Dictionary<long, long> d = new Dictionary<long, long>();
        long n = nums.Length;
        for (int i = 0; i < n; i++)
        {
            long tmp = nums[i] - i;
            if (d.ContainsKey(tmp))
            {
                d[tmp]++;
            }
            else
            {
                d[tmp] = 1;
            }
        }
        long total_pairs = (long)((n * (n - 1)) / 2);
        foreach (var item in d)
        {
            total_pairs -= (long)((item.Value * (item.Value - 1)) / 2);
        }
        return total_pairs;
    }
}