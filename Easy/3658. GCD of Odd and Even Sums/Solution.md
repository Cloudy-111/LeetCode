# Problem:

You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

sumOdd: the sum of the first n odd numbers.

sumEven: the sum of the first n even numbers.

Return the GCD of sumOdd and sumEven.

# Solution:

The first n odd numbers is 1, 3, ..., 2n - 1
Sum of those numbers is ((2n - 1 + 1) n) / 2 = n \* n

The first n even numbers is 2, 4, ..., 2n
Sum of those numbers is ((2n + 2) n) / 2 = n (n + 1)

# We use GCD algorythm to calculate 2 numbers above
