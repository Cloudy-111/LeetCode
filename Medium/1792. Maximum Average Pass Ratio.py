import heapq

# Ý tưởng chính bài này là học sinh đầu tiên được thêm vào 1 lớp nào đó sẽ làm cho tỉ lệ tổng thay đổi nhiều nhất
# Lớp nào đó mà chỉ cần thêm 1 học sinh thì sự thay đổi sẽ là lớn nhất
# Như vậy, chỉ cần tìm lớp mà thêm 1 học sinh thì tỉ lệ thay đổi lớn nhất, sau đó cứ lặp lại cho đến hết học sinh


# --> Dùng priority queue lưu sự thay đổi tỉ lệ khi 1 học sinh được thêm vào 1 lớp, mỗi 1 phần tử trong queue đó sẽ gồm sự thay đổi tỉ lệ và vị trí lớp

def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    pq = []
    heapq.heapify(pq)

    for i in range(len(classes)):
        passed = classes[i][0]
        total = classes[i][1]
        heapq.heappush(pq, (-(passed + 1) / (total + 1) + passed / total, i))

    while extraStudents:
        idx = heapq.heappop(pq)[1]
        classes[idx][0] += 1
        classes[idx][1] += 1
        passed = classes[idx][0]
        total = classes[idx][1]
        heapq.heappush(pq, (-(passed + 1) / (total + 1) + passed / total, idx))
        extraStudents -= 1

    res = 0
    while pq:
        idx = heapq.heappop(pq)[1]
        avg = classes[idx][0] / classes[idx][1]
        res += avg

    return float(format(res / len(classes), ".5f"))

# Có thể làm 1 cách ngắn gọn hơn, nhưng ý tưởng thì vẫn vậy:
# Lưu trong mỗi phần tử của priority queue gồm độ thay đổi tỉ lệ, số pass, total, lặp lại đến hết số học sinh và cập nhật heapq
# cuối cùng thì duyệt qua pass và total của priority queue đó là được


def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    classes = [(passed / total-(passed + 1)/(total + 1), passed, total)
               for passed, total in classes]
    heapq.heapify(classes)
    while extraStudents:
        _, passed, total = heapq.heappop(classes)
        heapq.heappush(classes, ((passed + 1) / (total + 1) -
                                 (passed + 2) / (total + 2), passed + 1, total + 1))
        extraStudents -= 1

    return sum([passed / total for _, passed, total in classes]) / len(classes)
