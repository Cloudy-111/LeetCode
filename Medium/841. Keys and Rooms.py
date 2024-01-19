class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.res = 1
        visit = [0] * len(rooms)
        visit[0] = 1

        def DFS(current):
            for i in rooms[current]:
                if visit[i] == 0:
                    self.res += 1
                    visit[i] = 1
                    DFS(i)
        DFS(0)
        return self.res == len(rooms)
