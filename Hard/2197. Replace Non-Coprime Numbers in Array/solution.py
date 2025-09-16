class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        current = nums[0]
        for num in nums[1:]:
            if self.GCD(current, num) > 1:
                current = self.LCM(current, num)
                while stack and self.GCD(current, stack[-1]) > 1:
                    current = self.LCM(current, stack.pop())
            else:
                stack.append(current)
                current = num

        stack.append(current)
        return stack
    
    def GCD(self, a, b):
        if a == 1 or b == 1: return 1
        while b > 0:
            tmp = b
            b = a % b
            a = tmp
        return a
    
    def LCM(self, a, b):
        return int(a * b / self.GCD(a, b))
