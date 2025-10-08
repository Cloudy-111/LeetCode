# Problem: [Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

# Solution:

First sight, we use Brute Force to calculate all couple can be made and compare to success
That is O(n^2) time complexity, impossible when n <= 10^5

### To reduce the time complexity to O(nlogn), we just need to find the first >= success / spells position in the non-decreasing sorted potions array
