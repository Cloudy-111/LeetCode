public class Solution
{
    public string ClearDigits(string s)
    {
        Stack<char> stack = new Stack<char>();
        string digits = "0123456789";
        foreach (char c in s)
        {
            if (!digits.Contains(c))
            {
                stack.Push(c);
            }
            else
            {
                stack.Pop();
            }
        }
        string result = new string(stack.Reverse().ToArray());
        return result;
    }
}

public class Solution
{
    public string ClearDigits(string s)
    {
        StringBuilder sb = new StringBuilder();
        foreach (char c in s)
        {
            if (!char.IsDigit(c))
            {
                sb.Append(c);
            }
            else
            {
                sb.Remove(sb.Length - 1, 1);
            }
        }
        return sb.ToString();
    }
}