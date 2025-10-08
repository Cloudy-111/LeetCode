public class Solution
{
    public int[] SuccessfulPairs(int[] spells, int[] potions, long success)
    {
        Array.Sort(potions);
        List<int> res = new List<int>();

        for (int i = 0; i < spells.Length; i++)
        {
            double target = (double)success / spells[i];
            int index = boundary_left(potions, target);
            res.Add(potions.Length - index);
        }

        return res.ToArray();
    }

    public int boundary_left(int[] potions, double target)
    {
        int l = 0, r = potions.Length;
        while (l < r)
        {
            int mid = (l + r) / 2;
            if (potions[mid] < target)
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }
}