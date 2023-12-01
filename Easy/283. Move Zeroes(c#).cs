public class Solution
{
    public void MoveZeroes(int[] nums)
    {
        int cnt = 0, zeros = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] != 0)
            {
                nums[cnt] = nums[i];
                cnt++;
            }
            else zeros++;
        }
        for (int i = 0; i < zeros; i++) nums[nums.Length - 1 - i] = 0;
    }
}