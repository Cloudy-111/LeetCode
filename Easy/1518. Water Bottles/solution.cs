public class Solution
{
    public int NumWaterBottles(int numBottles, int numExchange)
    {
        int res = 0;
        int additional = numBottles;
        while (numBottles >= numExchange)
        {
            res += additional;
            additional = numBottles / numExchange;
            int emptyBottles = numBottles % numExchange;
            numBottles = additional + emptyBottles;
        }
        return res + additional;
    }
}