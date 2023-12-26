class Solution:
    # chả cần lưu các điểm đã đi qua vào 1 set rồi duyệt từng bước đi một
    def isPathCrossing(self, path: str) -> bool:
        start = (0, 0)
        s = set([start])
        for i in path:
            x, y = start[0], start[1]
            if i == 'N':
                y += 1
            if i == 'S':
                y -= 1
            if i == 'E':
                x += 1
            if i == 'W':
                x -= 1
            start = (x, y)
            if start in s:
                return True
            else:
                s.add(start)
        return False
