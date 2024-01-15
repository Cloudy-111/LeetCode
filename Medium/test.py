
from collections import deque


def check(x, y):
    q = deque()
    q.append([x, 0])
    while q:
        t, cnt = q.popleft()
        if t == y:
            return cnt
        if t % 11 == 0:
            if t // 11 == y:
                return cnt + 1
            q.append([t // 11, cnt + 1])
        elif t % 5 == 0:
            if t // 5 == y:
                return cnt + 1
            q.append([t // 5, cnt + 1])
        if t - 1 == y:
            return cnt + 1
        q.append([t - 1, cnt + 1])
        if t + 1 == y:
            return cnt + 1
        q.append([t + 1, cnt + 1])


x, y = [1, 21]
print(check(x, y))
