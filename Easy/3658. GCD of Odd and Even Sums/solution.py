class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n * n
        sumEven = n * (n + 1)

        def gcd(a, b):
            while b > 0:
                tmp = b
                b = a % b
                a = tmp
            return a
        return gcd(sumOdd, sumEven)
