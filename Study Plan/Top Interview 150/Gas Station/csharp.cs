public class Solution
{
    public int CanCompleteCircuit(int[] gas, int[] cost)
    {
        int currentGas = gas[0];
        int res = 0;
        int sumGas = gas[0];
        int sumCost = cost[0];
        for (int i = 1; i < gas.Length; i++)
        {
            currentGas -= cost[i - 1];
            sumGas += gas[i];
            sumCost += cost[i];
            if (currentGas < 0)
            {
                res = i;
                currentGas = gas[i];
            }
            else
            {
                currentGas += gas[i];
            }
        }
        if (sumGas < sumCost) return -1;
        return res;
    }
}