public class Solution {
    public IList<int> ReplaceNonCoprimes(int[] nums) {
        Stack<int> stack = new Stack<int>();
        int current = nums[0];
        for(int i = 1; i < nums.Length; i++){
            int gcd = GCD(current, nums[i]);
            if(gcd > 1){
                current = current / gcd * nums[i];

                while(stack.Count > 0 && GCD(current, stack.Peek()) > 1){
                    current = LCM(current, stack.Pop());
                }
            } else{
                stack.Push(current);
                current = nums[i];
            }
        }
        stack.Push(current);
        
        IList<int> res = stack.Reverse().ToList();
        return res;
    }

    public int GCD(int a, int b){
        if(a == 1 || b == 1) return 1;
        while(b > 0){
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    } 

    public int LCM(int a, int b){
        return a / GCD(a, b) * b;
    }
}