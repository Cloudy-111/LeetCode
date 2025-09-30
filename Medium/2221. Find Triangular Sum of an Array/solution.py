class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return (nums[0] + nums[1]) % 10
        n = len(nums)

        pascal_triangle = [[0] * (n - 1) for _ in range(n - 2)]
        res = nums[0]

        pascal_triangle[0][0] = 2
        pascal_triangle[0][1] = 1

        for i in range(1, n - 2):
            pascal_triangle[i][0] = i + 2
            pascal_triangle[i][i + 1] = 1
            for j in range(1, i + 1):
                pascal_triangle[i][j] = pascal_triangle[i -
                                                        1][j - 1] + pascal_triangle[i - 1][j]
        # print(pascal_triangle)
        for i in range(n - 1):
            res += pascal_triangle[-1][i] * nums[i + 1]
        return res % 10

# No need to store all elements of whole Pascal Triangle


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return (nums[0] + nums[1]) % 10
        n = len(nums) - 1

        pascal = [1]
        res = nums[-1] + nums[0]
        for i in range(1, n):
            pascal.append(pascal[-1] * (n - i + 1) // i)
            res += pascal[-1] * nums[i]

        print(pascal)
        return res % 10

# No need to store all elements of last row of Pascal Triangle


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return (nums[0] + nums[1]) % 10
        n = len(nums) - 1

        pascal = 1
        res = nums[-1] + nums[0]
        for i in range(1, n):
            pascal = pascal * (n - i + 1) // i
            res += pascal * nums[i]

        return res % 10
