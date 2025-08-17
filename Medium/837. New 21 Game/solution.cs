public class Solution {
    public double New21Game(int n, int k, int maxPts) {
        if( k == 0 || n >= k + maxPts - 1) {
            return 1.0;
        }

        double[] dp = new double[n + maxPts + 1];
        for(int i = k; i <= n; i += 1){
            dp[i] = 1.0;
        }

        double windowSumProbability = 0.0;
        for(int i = k; i <= k + maxPts; i += 1){
            windowSumProbability += dp[i];
        }

        dp[k - 1] = windowSumProbability / maxPts;
        for(int i = k - 2; i >= 0; i -= 1){
            windowSumProbability = windowSumProbability - dp[i + maxPts + 1] + dp[i + 1];
            dp[i] = windowSumProbability / maxPts;
        }

        return dp[0];
    }
}