public class Solution
{
    public int MinOperations(int[] nums, int k)
    {
        PriorityQueue<long, long> pq = new PriorityQueue<long, long>();
        int res = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            pq.Enqueue(nums[i], nums[i]);
        }
        while (pq.Count >= 2 && pq.Peek() < k)
        {
            long a = pq.Dequeue();
            long b = pq.Dequeue();
            long sum = a * 2 + b;
            pq.Enqueue(sum, sum);
            res++;
        }
        return res;
    }
}