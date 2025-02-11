public class Solution
{
    public int RomanToInt(string s)
    {
        Dictionary<char, int> roman = new Dictionary<char, int>
        {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int res = 0;
        for (int i = 0; i < s.Length - 1; i++)
        {
            if (roman[s[i]] < roman[s[i + 1]])
            {
                res -= roman[s[i]];
            }
            else
            {
                res += roman[s[i]];
            }
        }
        return res + roman[s[s.Length - 1]];
    }
}