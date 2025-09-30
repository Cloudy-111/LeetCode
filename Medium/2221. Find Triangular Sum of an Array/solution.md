# Problem: Find Triangular Sum of an Array

You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.

For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.

Replace the array nums with newNums.

Repeat the entire process starting from step 1.

Return the triangular sum of nums.

# Solution:

At first glance, we think that we are doing it repeatedly until the array has only 1 element left, but that way takes too much time and memory.

### We realize that the final sum will be in the form of the last row of Pascal's triangle

For example:

with the array [a,b,c,d,e]

When we do it in turn according to the problem description, we get the final sum as

### a + 4b + 6c + 4d + e

The coefficients of each element are the values ​​in the last row of Pascal's triangle with n = 4

### Thus, we only need to know the values ​​of the elements in the last row of Pascal's triangle

In Pascal's triangle, the numbers in row n are:

### 0Cn, 1Cn, 2Cn, ... , nCn

so with the recurrence formula of the combination:

## kCn = (k - 1)Cn \* ((n - k + 1) / k)

We will calculate all the values ​​of the last row of Pascal's triangle

Time Complexity: O(n)
Space: O(1)

## There is only one problem here is that when n is large(to million), the combinations are also large, so we have to Handle overflow with BigInteger or modulo combinations(kCn mod 10)
