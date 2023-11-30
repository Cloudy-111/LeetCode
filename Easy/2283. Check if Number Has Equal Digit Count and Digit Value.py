class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if ord(num[i]) - ord('0') != num.count(str(i)):
                return False
        return True
