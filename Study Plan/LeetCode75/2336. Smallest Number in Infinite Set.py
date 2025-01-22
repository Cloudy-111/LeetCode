import heapq

# self.start là biến để lưu giá trị bắt đầu của dãy số, mặc định là 1
# self.arr là mảng để lưu các số đã thêm vào, mặc định là rỗng
# khi thực hiện hàm popSmallest, nếu mảng rỗng có nghĩa là chưa có số nào được thêm vào, và sẽ pop ra số đầu tiên là self.start, tăng nó lên 1
# Ngược lại, nếu mảng đang có số thì sẽ pop ra số nhỏ nhất trong mảng
# Với hàm addBack, nếu số đã tồn tại trong mảng thì không thêm vào, ngược lại nếu số nhỏ hơn self.start thì thêm vào mảng vì số nhỏ hơn đương nhiên đã được pop ra khỏi InfiniteSet
# số lớn hơn self.start thì có nghĩa là nó vẫn nằm trong InfiniteSet


class SmallestInfiniteSet:

    def __init__(self):
        self.arr = []
        self.start = 1

    def popSmallest(self) -> int:
        if len(self.arr) == 0:
            self.start += 1
            return self.start - 1
        else:
            return heapq.heappop(self.arr)

    def addBack(self, num: int) -> None:
        if num in set(self.arr):
            return
        elif num < self.start:
            heapq.heappush(self.arr, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
