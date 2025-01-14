class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        arr = [0] * (n + 1)
        res = [0]
        for i in range(len(A)):
            if A[i] == B[i]:
                res.append(res[-1] + 1)
                arr[A[i]] = 1
            else:
                res.append(arr[A[i]] + arr[B[i]] + res[-1] )
                arr[A[i]] = 1
                arr[B[i]] = 1
        return res[1:]
            