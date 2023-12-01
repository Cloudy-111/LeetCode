public class Solution
{
    public bool IsSubsequence(string s, string t)
    {
        int a = 0, b = 0, cnt = 0;
        while (a < s.Length && b < t.Length)
        {
            if (s[a] == t[b])
            {
                a++; b++; cnt++;
            }
            else b++;
        }
        return cnt == s.Length;
    }
}