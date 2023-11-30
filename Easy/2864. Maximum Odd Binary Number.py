class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero = s.count('0')
        one = s.count('1')
        return '1' * (one - 1) + '0' * zero + '1'
