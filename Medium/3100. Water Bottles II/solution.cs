public class Solution
{
    public int MaxBottlesDrunk(int numBottles, int numExchange)
    {
        int res = numBottles;
        int emptyBottles = numBottles;

        while (emptyBottles >= numExchange)
        {
            res += 1;
            emptyBottles = emptyBottles - numExchange + 1;
            numExchange += 1;
        }

        return res;
    }
}