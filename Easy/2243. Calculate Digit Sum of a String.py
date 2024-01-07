class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def group(a):
            return str(sum(int(x) for x in a))
        while len(s) > k:
            res = []
            for i in range(0, len(s), k):
                res.append(group(s[i: i+k]))
            s = ''.join(res)
        return s
