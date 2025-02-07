public class Solution
{
    public int[] QueryResults(int limit, int[][] queries)
    {
        Dictionary<int, int> d = new Dictionary<int, int>();
        Dictionary<int, int> seen = new Dictionary<int, int>();
        int tmp = 0;
        List<int> res = new List<int>();
        foreach (var query in queries)
        {
            int ball = query[0];
            int color = query[1];

            int prev_color = d.GetValueOrDefault(ball, 0);
            if (prev_color != color)
            {
                if (prev_color > 0)
                {
                    if (seen.ContainsKey(prev_color))
                    {
                        seen[prev_color]--;
                        if (seen[prev_color] == 0)
                        {
                            seen.Remove(prev_color);
                            tmp -= 1;
                        }
                    }
                }
                if (!seen.ContainsKey(color))
                    tmp += 1;
                if (!seen.ContainsKey(color))
                    seen[color] = 0;
                seen[color] += 1;
            }
            d[ball] = color;
            res.Add(tmp);
        }
        return res.ToArray();
    }
}