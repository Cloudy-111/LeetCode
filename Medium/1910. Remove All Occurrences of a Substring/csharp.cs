public class Solution
{
    public string RemoveOccurrences(string s, string part)
    {
        while ((index = s.IndexOf(part)) != -1)
        {
            s = s.Remove(index, part.Length);
            // s = s[..index] + s[(index + part.Length)..];
        }
        return s;
    }
}