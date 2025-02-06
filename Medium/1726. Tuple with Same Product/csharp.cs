public class Solution
{
    public int TupleSameProduct(int[] nums)
    {
        if (nums.Length < 4) return 0;
        int cnt = 0;
        Dictionary<int, int> map = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++)
            {
                int product = nums[i] * nums[j];
                if (map.ContainsKey(product))
                {
                    cnt += map[product];
                    map[product]++;
                }
                if (!map.ContainsKey(product))
                {
                    map.Add(product, 1);
                }
            }
        }
        return cnt * 8;
    }
}