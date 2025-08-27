public class Solution {
    public bool PartitionArray(int[] nums, int k) {
        int n = nums.Length;
        if(n % k != 0)return false;

        int num_group = n / k;

        Dictionary<int, int> d = new Dictionary<int, int>();
        for(int i = 0; i < n; i++){
            if(!d.ContainsKey(nums[i])){
                d[nums[i]] = 1;
            } else {
                d[nums[i]] += 1;
            }
        }

        foreach(int v in d.Values){
            if(v > num_group) return false;
        }
        return true;

    }
}