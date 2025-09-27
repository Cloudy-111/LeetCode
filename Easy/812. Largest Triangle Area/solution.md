# Problem

Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

# Solution:

## Approach 1: Brute force on points, use all points to calculate area and get max

## Approach 2: Find Convex Hull of Points, and Brute force on that Convex Hull

- Sort points array by x[0] and x[1]
- Initialize lower_hull and upper_hull to store points of upper and lower halves of the convex hull
- Traverse from left to right to construct the lower hul
- For each new point, check if the added point is still convex. If not, pop the previous point
- Traverse from right to left to construct the upper hull similarly
- Combine the two halves and get the convex hull

### Check if the added point is still convex:

If we have 3 point A(x1, y1), B(x2, y2), C(x3, y3) then scalar product of them is:

### S = (x2 ​− x1) \* (y3 − y1) − (y2 − y1) \* (x3 − x1)

if S < 0: C is on the right side of line AB
if S > 0: C is on the left side of line AB
if S == 0: C lies on line AB

We traverse from left to right of the sorted array of points, so we always go left or straight from the lowest point to the highest point (S >= 0) to create the lower_hull
and the same goes for the reverse

We traverse from left to right of the sorted array, so we always go left or straight from the lowest point to the highest point (S >= 0) to create the lower_hull
and vice versa to create upper_hull

The remaining task is to traverse all the 3 points in the created convex hull
