from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q1 = deque()
        q2 = deque()
        for i in range(len(senate)):
            if senate[i] == 'D':
                q1.append(i)
            else:
                q2.append(i)
        tmp = len(senate)

        while q1 and q2:
            s1, s2 = q1.popleft(), q2.popleft()
            if s1 < s2:
                q1.append(s1 + tmp)
            else:
                q2.append(s2 + tmp)
        if q1.empty():
            return 'Radiant'
        else:
            return 'Dire'
