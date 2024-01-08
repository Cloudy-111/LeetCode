class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for i in logs:
            if i == './':
                pass
            elif i == '../':
                if res > 0:
                    res -= 1
            else:
                res += 1
        return res
