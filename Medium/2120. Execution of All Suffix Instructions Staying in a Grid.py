class Solution:

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []

        def move(direct, Px, Py):
            if direct == 'L':
                Py -= 1
            if direct == 'R':
                Py += 1
            if direct == 'U':
                Px -= 1
            if direct == 'D':
                Px += 1
            return list([Px, Py])

        for i in range(len(s)):
            j = i
            cnt = 0
            next = move(s[j], startPos[0], startPos[1])
            while (j < len(s) and 0 <= next[0] < n and 0 <= next[1] < n):
                cnt += 1
                j += 1
                if j < len(s):
                    next = move(s[j], next[0], next[1])
            res.append(cnt)
        return res
