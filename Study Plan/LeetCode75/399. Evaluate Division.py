class Solution:
    # Bài toán có thể được giải theo phương pháp đồ thị, coi như mỗi biến là 1 đỉnh, value sẽ là trọng số đường đi giữa 2 đỉnh
    # Sử dụng union find để gán trọng số của mỗi đỉnh là kết quả trọng số từ đỉnh đó tới gốc, như vậy, khi tính trọng số giữa 2 đỉnh cùng gốc thì chỉ cần chia cho nhau là được
    def __init__(self):
        self.parent = {}

    def initilize(self, equations):
        for x, y in equations:
            # Ban đầu thì khởi tạo gốc mỗi đỉnh là chính nó và có trọng số là 1
            self.parent[x] = (x, 1.0)
            self.parent[y] = (y, 1.0)

    def find_root(self, x):
        parent, value = self.parent[x]
        if parent != x:
            root, root_value = self.find_root(parent)
            # value biểu thị tỷ lệ giữa x và gốc của nó. Nếu phải đi qua nhiều bước để tìm gốc, value sẽ được nhân dần với các trọng số trên đường đi.
            self.parent[x] = (root, value * root_value)
        return self.parent[x]

    def union_join(self, x, y, value):
        # val_x là tỉ lệ giữa x và gốc đại diện của nó
        root_x, val_x = self.find_root(x)
        # val_y là tỉ lệ giữa y và gốc đại diện của nó
        root_y, val_y = self.find_root(y)
        if root_x != root_y:
            # Hợp nhất 2 gốc lại sao cho tỉ lệ giữa x và y không thay đổi(value)
            # ví dụ với đỉnh a có gốc là (a, 1), b có (b, 1) và a / b = 2 thì sau khi hợp nhất gốc a và gốc b thì trọng số mới của gốc đại diện b = trọng số a / trọng số b * tỉ lệ = 2
            self.parent[root_y] = (root_x, val_x / val_y * value)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.initilize(equations)

        for i in range(len(equations)):
            x, y = equations[i]
            val = values[i]
            self.union_join(x, y, val)

        res = []
        for x, y in queries:
            if x not in self.parent or y not in self.parent:
                res.append(-1.0)
            else:
                root_x, val_x = self.find_root(x)
                root_y, val_y = self.find_root(y)
                if root_x != root_y:
                    res.append(-1.0)
                else:
                    res.append(val_y / val_x)
        return res
