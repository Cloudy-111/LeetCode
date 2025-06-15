public class Solution
{
    public bool BackspaceCompare(string s, string t)
    {
        Stack<char> stackS = new Stack<char>();
        Stack<char> stackT = new Stack<char>();

        foreach (char c in s)
        {
            if (stackS.Count() > 0 && c == '#')
            {
                stackS.Pop();
            }
            else if (c != '#')
            {
                stackS.Push(c);
            }
        }
        foreach (char c in t)
        {
            if (stackT.Count() > 0 && c == '#')
            {
                stackT.Pop();
            }
            else if (c != '#')
            {
                stackT.Push(c);
            }
        }

        string resultS = new string(stackS.ToArray().Reverse().ToArray());
        string resultT = new string(stackT.ToArray().Reverse().ToArray());

        return resultS == resultT;
    }
}