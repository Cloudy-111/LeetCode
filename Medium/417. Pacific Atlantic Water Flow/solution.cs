public class Solution
{
    public IList<IList<int>> PacificAtlantic(int[][] heights)
    {
        int n = heights.Length, m = heights[0].Length;

        int[,] can_in_Pacific = new int[n, m];
        int[,] can_in_Atlantis = new int[n, m];

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (i == 0 || j == 0) can_in_Pacific[i, j] = 1;
                if (i == n - 1 || j == m - 1) can_in_Atlantis[i, j] = 1;
            }
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (i == 0 || j == 0) BFS(can_in_Pacific, i, j, heights);
                if (i == n - 1 || j == m - 1) BFS(can_in_Atlantis, i, j, heights);
            }
        }

        var res = new List<IList<int>>();
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (can_in_Pacific[i, j] == 1 && can_in_Atlantis[i, j] == 1)
                {
                    res.Add(new List<int> { i, j });
                }
            }
        }

        return res;
    }

    public void BFS(int[,] matrix, int i, int j, int[][] heights)
    {
        int n = heights.Length, m = heights[0].Length;

        int[] moveX = { -1, 0, 1, 0 };
        int[] moveY = { 0, -1, 0, 1 };

        var queue = new Queue<(int x, int y)>();
        queue.Enqueue((i, j));

        while (queue.Count > 0)
        {
            var (x, y) = queue.Dequeue();
            for (int k = 0; k < 4; k++)
            {
                int newX = x + moveX[k];
                int newY = y + moveY[k];

                if (newX >= 0 && newX < n && newY >= 0 && newY < m && matrix[newX, newY] == 0)
                {
                    if (heights[x][y] <= heights[newX][newY])
                    {
                        queue.Enqueue((newX, newY));
                        matrix[newX, newY] = 1;
                    }
                }
            }
        }
    }
}