# Solution:

### Notice that n is reference by 4**x, which mean 2 ** (2x)

That mean, n can be represented by 1000000.... (number of 0s is even)
And n - 1 can be represented by 011111111..... (number of 1s equal number of 0s of bit n)

### So, n & (n - 1) == 0 if n is power of 4 (This is First condition)

### And every satisfied number n(power of 4) have this: n - 1 % 3 == 0(Second Condition)

So with 2 conditions above, We can determind n is power of 4 or not
