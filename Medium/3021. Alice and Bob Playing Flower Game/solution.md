# Problem:

Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are x flowers in the first lane between Alice and Bob, and y flowers in the second lane between them.
The game proceeds as follows:

Alice takes the first turn.
In each turn, a player must choose either one of the lane and pick one flower from that side.
At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

Alice must win the game according to the described rules.
The number of flowers x in the first lane must be in the range [1,n].
The number of flowers y in the second lane must be in the range [1,m].
Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

# Solution: This problem is much easier than it look

To get the pair x, y that satisfies the problem: Alice goes first, Alice always wins, then the sum of x + y will always have to be an odd number

And if the sum of 2 numbers is odd, then one of the two numbers is even, the other is odd
So we just need to calculate the sum of the pairs created from even and odd pairs, which will be the sum of the pairs created from odd numbers > 1, < n and even numbers > 1, < m and vice versa.
