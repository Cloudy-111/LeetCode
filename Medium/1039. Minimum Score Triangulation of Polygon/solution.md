# Problem: Minimum Score Triangulation of Polygon

You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

Return the minimum possible score that you can achieve with some triangulation of the polygon.

# Solution:

This is a problem of finding the minimum value (optimum), so we think of the greedy and dynamic programming methods.

With greed, there is only a local optimal method (because considering all cases, all ways of division are certainly not feasible), that is, choosing the triangle with the smallest weight first and then gradually with the next triangles, but if choosing the triangle with the smallest weight first, the final result is not necessarily the smallest.

### This problem has an Optimal Substructure:

If choosing a triangle (i, j, k) in the division process, the remaining part of the problem is:

- divide the segment from i → k

- divide the segment from k → j

This is the basic property of DP: the large problem can be divided into independent subproblems, the optimal solution of the large problem will include the optimal solutions of the subproblems.

So with the above method, to calculate the optimal result when choosing 2 vertices i and j, we choose some k between the 2 vertices and divide it into 2 parts from i to k and k to j and triangle (i, j, k)

## Suppose we consider a polygon segment from vertex i to vertex j (clockwise).

- If j - i < 2 then no triangle can be created.

- If j - i == 2 then there is exactly 1 triangle (i, j, k).

### Choose k as the division point, then we have 2 sub-parts and add the triangle weight (i, j, k).

dp[i][j] = min( dp[i][k] + dp[k][j] + values[i] \* values[j] \* values[k] )

### dp[i][j] is the smallest cost when dividing the segment from i to j.
