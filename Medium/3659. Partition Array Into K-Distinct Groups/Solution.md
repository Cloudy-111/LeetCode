# Problem:

You are given an integer array nums and an integer k.

Your task is to determine whether it is possible to partition all elements of nums into one or more groups such that:

Each group contains exactly k distinct elements.
Each element in nums must be assigned to exactly one group.
Return true if such a partition is possible, otherwise return false.

# Solution:

- For the first condition: if the size of nums is not divisible by k, we can immediately return False.
- For the second condition: each element in nums must be assigned to exactly one group.

This means each group cannot contain duplicate numbers. Therefore, we count the frequency of each number.
If any number appears more times than the number of possible groups, we must return False.
