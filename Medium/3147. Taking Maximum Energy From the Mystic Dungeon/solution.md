# Problem: [Taking Maximum Energy From the Mystic Dungeon](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/)

In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.

In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.

You are given an array energy and an integer k. Return the maximum possible energy you can gain.

Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.

# Solution:

We can start from any magician and keep jumping forward by k steps until we go out of the array.

Our goal is to find the starting position that gives the maximum total energy collected along the path.

If we think in reverse — from the end of the array to the beginning —
for each magician i, the total energy we can collect starting at i equals:

### energy[i] + energy[i + k] + energy[i + 2k] + ...

When we process magician i, if i + k is still inside the array, we already know the best total energy starting from i + k.

Therefore, we can reuse it:

### energy[i] = energy[i] + energy[i + k]

This makes energy[i] store the total energy obtainable starting from i.

During the process, we keep track of the maximum value among all energy[i], since that represents the best possible starting point.

This approach ensures each element is visited once,

so the total time complexity is O(n) and space complexity is O(1).
