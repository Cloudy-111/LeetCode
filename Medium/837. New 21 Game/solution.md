# Solution: New 21 Game

## Problem Summary:

This problem requires us to calculate the probability that Alice's total points (after drawing >= k points) <= n

- Alice starts at 0 points
- Each turn, Alice will draw 1 number in [1, maxPts] with equal probability and accumulate those points
- Alice plays when the total points >= k
- Calculate the probability that Alice's total points after finishing the game <= n

## Key Observations:

So we can see that when Alice has a score >= k and <= n, Alice will win
And when Alice's score < k, Alice will draw another number

Thus the problem will be reduced to the Probability that Alice will win when she has x points

- When k <= x <= n, the probability that Alice wins (total score >= k and <= n) is 1
- When x < k, Alice will draw another number in [1, maxPts]
  Because these values have equal probability (P = 1 / maxPts), so the probability that Alice wins when she has x points is the average probability that Alice wins in the draws in [1, maxPts]

So the problem will be reduced to calculating the value of dp[0] (where dp is the array of probabilities that Alice wins when she has x points)

dp[x] = 1 / maxPts \* (dp[x + 1] + dp[x + 2] + ... + dp[x + maxPts])

### With the above formula, it will take O(maxPts) for the inner loop and take O(k) for dp[x] -> O(k \* maxPts)

so we will apply a sliding window, calculate first the part dp[x + 1] + dp[x + 2] + ... + dp[x + maxPts], then gradually shift the window back to calculate the previous dp and gradually to 0
