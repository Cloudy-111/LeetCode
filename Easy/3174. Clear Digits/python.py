class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        digits = "0123456789"
        for i in s:
            if i not in digits:
                stack.append(i)
            else:
                stack.pop()
        return ''.join(stack)


class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for c in s:
            if c.isalpha():
                res.append(c)
            else:
                res.pop()
        return ''.join(res)
