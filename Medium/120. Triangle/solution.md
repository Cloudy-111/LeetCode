# Problem

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Solution: Basic Dynamic Programming

## Approach 1: Use Top-down solution

- At each cell, we have to choose to go down left or right
- To calculate the shortest path from top to bottom, we will have to remember all the previous choices
- If we do it directly from top to bottom, we need a 2D DP array or recursion + memoization to store the result at each cell, because in the middle we do not know what will happen “below”

## Approach 2: Use Bottom-up solution

- In the last row (bottom), the smallest result is the cell value (since there is no next step)
- Moving up the row, the smallest path in a cell depends only on the 2 cells immediately below it
- This allows us to work our way back up to the top
- When we reach the first row, dp[0] is the answer
