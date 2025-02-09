public class NumberContainers
{
    // SortedSet hoạt động giống như set nhưng nó sắp xếp các phần tử theo thứ tự tăng dần
    private Dictionary<int, SortedSet<int>> d = new Dictionary<int, SortedSet<int>>();
    private Dictionary<int, int> index = new Dictionary<int, int>();
    public NumberContainers()
    {
        d = new Dictionary<int, SortedSet<int>>();
        index = new Dictionary<int, int>();
    }

    public void Change(int index, int number)
    {
        if (!d.ContainsKey(number))
        {
            d[number] = new SortedSet<int>();
        }
        if (this.index.ContainsKey(index))
        {
            int oldNum = this.index[index];
            d[oldNum].Remove(index);
        }
        d[number].Add(index);
        this.index[index] = number;
    }

    public int Find(int number)
    {
        if (!d.ContainsKey(number) || d[number].Count == 0)
        {
            return -1;
        }
        return d[number].First();
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.Change(index,number);
 * int param_2 = obj.Find(number);
 */