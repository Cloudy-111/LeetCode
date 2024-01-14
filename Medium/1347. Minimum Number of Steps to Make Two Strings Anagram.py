class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for i in s:
            dic1[i] += 1
        for i in t:
            dic2[i] += 1
        res = 0
        for i in dic2:
            if dic2[i] > dic1[i]:
                res += dic2[i] - dic1[i]
        return res
