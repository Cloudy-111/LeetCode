public class Solution {
    public int MakeTheIntegerZero(int num1, int num2) {
        for(int k = 0; k < 61; k++){
            long temp = (long)num1 - k * (long)num2; 
            if(temp == 1 && k > 1)return -1;
            if(temp <= 0) return -1;
            int num_operations = count_bit(temp);
            if(num_operations <= k) return k;
        }
        return -1;
    }

    public int count_bit(long n){
        int res = 0;
        while(n > 0){
            if(n % 2 == 1) res += 1;
            n >>= 1;
        }
        return res;
    }
}