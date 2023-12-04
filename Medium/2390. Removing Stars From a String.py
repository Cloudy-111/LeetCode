class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i == '*' and len(res) > 0:
                res.pop()
            else:
                res.append(i)
        if len(res) == 0:
            return ''
        else:
            return ''.join(res)
