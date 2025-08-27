public class Solution {
    public int GcdOfOddEvenSums(int n) {
        int sumOdd = n * n;
        int sumEven = n * (n + 1);

        return GCD(sumOdd, sumEven);
    }

    public int GCD(int a, int b){
        while(b > 0){
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }
}