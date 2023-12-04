from collections import deque


class RecentCounter:

    def __init__(self):
        self.qu = deque()

    def ping(self, t: int) -> int:
        self.qu.append(t)
        while t - self.qu[0] > 3000:
            self.qu.popleft()
        return len(self.qu)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
