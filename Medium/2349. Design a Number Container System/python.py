import heapq

# Ý tưởng đầu: với mỗi số được "change", ta thêm nó vào set tương ứng với số đó trong dict d.
# Nếu index đó có số khác trước đó, ta loại bỏ index đó khỏi set của số đó và thêm index mới vào
# gán lại index đó với số mới.
# Vói hàm find, ta trả về index nhỏ nhất trong set của số đó.
# Dùng heapq để tìm index nhỏ nhất trong set.
# Nhưng heapq không hỗ trợ với set, nên ta chuyển set sang list trước khi dùng heapq(O(n)) -> TLE


class NumberContainers:

    def __init__(self):
        self.d = dict()
        self.index = dict()

    def change(self, index: int, number: int) -> None:
        if number not in self.d:
            self.d[number] = set()
        if index in self.index:
            self.d[self.index[index]].remove(index)
        self.d[number].add(index)
        self.index[index] = number

    def find(self, number: int) -> int:
        if number not in self.d or len(self.d[number]) == 0:
            return -1
        l = list(self.d[number])
        heapq.heapify(l)
        return l[0]

# Từ ý tưởng trên, ta thấy rằng ta không cần phải chuyển set sang list trước khi dùng heapq mà ta sẽ heapq nó luôn
# từ đó giảm độ phức tạp từ O(n) xuống O(logn), set dùng để kiểm tra xem số đó đã xuất hiện hay chưa, nếu có rồi thì loại index của nó (giống self.d ở ý trên)
# Nếu 1 số đã xuất hiện tại 1 ví trí nào đó, ta sẽ loại bỏ vị trí đó ra khỏi tập hợp set của nó


class NumberContainers:

    def __init__(self):
        self.d = dict()
        self.index = dict()
        self.seen = dict()

    def change(self, index: int, number: int) -> None:
        if number not in self.d:
            self.d[number] = []
            self.seen[number] = set()

        if index in self.index:
            old_num = self.index[index]
            if old_num in self.seen:
                self.seen[old_num].discard(index)

        heapq.heappush(self.d[number], index)
        self.seen[number].add(index)
        self.index[index] = number  # Cập nhật số mới cho index

    def find(self, number: int) -> int:
        if number not in self.d or not self.d[number]:
            return -1
        # Loại bỏ các index đã được thay sang các number khác(nghĩa là sẽ không có trong set seen)
        while self.d[number] and self.d[number][0] not in self.seen[number]:
            heapq.heappop(self.d[number])

        return self.d[number][0] if self.d[number] else -1
