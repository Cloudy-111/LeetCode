public class Solution {
    public int MaximumEnergy(int[] energy, int k) {
        int n = energy.Length;
        int res = Int32.MinValue;

        for(int i = n - 1; i >= 0; i--){
            if(i < n - k){
                energy[i] = energy[i] + energy[i + k];
            }
            res = Math.Max(res, energy[i]);
        }

        return res;
    }
}