class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0:
            if num[i] in '13579':
                break
            i -= 1
        return num[: i + 1]
