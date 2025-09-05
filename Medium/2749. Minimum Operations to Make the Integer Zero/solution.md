# Problem:

You are given two integers num1 and num2.

In one operation, you can choose integer i in the range [0, 60] and subtract 2^i + num2 from num1.

Return the integer denoting the minimum number of operations needed to make num1 equal to 0.

If it is impossible to make num1 equal to 0, return -1.

# Solution:

If it is possible from the problem, we have an equation:

## num1 - (num2 + 2^i1) - (num2 + 2^i2) - (num2 + 2^i3) - ... - (num2 + 2^ik) = 0

(i1, i2, ..., ik in [0, 60])

## -> num1 - k \* num2 = 2^i1 + 2^i2 + ... + 2^ik

k can only belong to [0, 60], so we can iterate k from 0 to 60 to find the result

Now, the remaining problem is the right side. We call sum of the right side is equal X

### Notice that, the right side of the expression is very similar to the binary representation of a number.

Example:

n = 9 = 2^3 + 2^0 -> bit representation: 1001

n = 15 = 2^3 + 2^2 + 2^1 + 2^0 -> bit representation: 1111

So X can be represented as the sum of powers of 2 as the representation to find the binary form of X, except that the terms in the sum can be the same

## Example:

n = 9 = 2^3 + 2^0 = 2^2 + 2^2 + 2^0

## Can X be expressed as the sum of \*\*exactly k powers of 2?

Let x = number of 1 bits in the binary representation of X.

- If x > k then X will never be represented by k powers of 2
- If x is equal to k then it will return k because it will definitely be represented correctly
- But if x < k, we can split larger powers into smaller ones until we reach k terms

### Note that there is a special case that if X == 1, k > 1, then X will be represented as 2^0, it cannot be decomposed into the sum of 2 numbers with smaller exponents then we will return -1
