class RandomizedSet:

    def __init__(self):
        self.dic = defaultdict(int)

    def insert(self, val: int) -> bool:
        if self.dic[val] == 0:
            self.dic[val] += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.dic[val] > 0:
            self.dic[val] -= 1
            return True
        return False

    def getRandom(self) -> int:
        key = random.choice([k for k, v in self.dic.items() if v > 0])  # O(n)
        return key


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

    # với cách O(1), ta tạo 1 dict có key là số thứ tự số được thêm vào, val là giá trị số đó
    # như vậy, khi getRandom, ta chỉ cần random số từ 0 cho đến số thứ tự max lúc đó thôi, O(1)
    # vì đây là tập hợp(set) nên ta không cần thêm số đã có vào, cần 1 dic khác để kiểm tra xem số đó đã xuất hiện trước hay chưa


    def __init__(self):
        self.dic = {}  # theo dõi số lượng số được đưa vào
        self.invertDict = {}  # theo dõi xem số đã có hay chưa
        self.numsElement = 0

    def insert(self, val: int) -> bool:
        if val in self.invertDict:
            return False
        self.dic[self.numsElement] = val
        self.invertDict[val] = self.numsElement
        self.numsElement += 1
        return True

    # khi remove là việc loại phần tử đó ra, lấy phần tử đó ra, thay vị trí đó bằng phần tử cuối cùng, sau đó xóa phần tử cuối cùng
    # nếu nó là phần tử cuối cùng thì xóa nó luôn
    # giảm số lượng số đi 1
    def remove(self, val: int) -> bool:
        if val not in self.invertDict:
            return False
        # xác định được vị trí mà bỏ phần tử có giá trị val
        index = self.invertDict.pop(val)
        self.dic.pop(index)  # loại bỏ vị trí đó
        if index != self.numsElement - 1:
            self.invertDict[self.dic[self.numsElement - 1]] = index
            self.dic[index] = self.dic[self.numsElement - 1]
            self.dic.pop(self.numsElement - 1)
        self.numsElement -= 1
        return True

    def getRandom(self) -> int:
        # lấy random các vị trí từ [0, self.numsElement - 1]
        index = floor(random.random() * self.numsElement)
        return self.dic[index]
