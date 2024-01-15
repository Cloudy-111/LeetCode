class Solution:
    # XOR tất cả số trong mảng rồi so sánh với số K(ở dạng biểu diễn bit xem có bao nhiêu vị trí mà nó khác nhau)
    def minOperations(self, nums: List[int], k: int) -> int:
        xorNums = 0
        for i in nums:
            xorNums ^= i
        res = 0
        binaryXorNums = bin(xorNums)[2:]
        binaryK = bin(k)[2:]
        if len(binaryXorNums) < len(binaryK):
            binaryXorNums = '0' * \
                (len(binaryK) - len(binaryXorNums)) + binaryXorNums
        else:
            binaryK = '0' * (len(binaryXorNums) - len(binaryK)) + binaryK
        for i in range(len(binaryXorNums)):
            if binaryXorNums[i] != binaryK[i]:
                res += 1
        return res
