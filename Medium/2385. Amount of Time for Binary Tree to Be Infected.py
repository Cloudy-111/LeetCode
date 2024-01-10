# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # đưa cây về đồ thị vô hướng(danh sách kề) rồi BFS
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root.left and not root.right:
            return 0
        self.adj = defaultdict(set)

        def travesal(root):
            if not root:
                return
            if root.left:
                self.adj[root.val].add(root.left.val)
                self.adj[root.left.val].add(root.val)
                travesal(root.left)
            if root.right:
                self.adj[root.val].add(root.right.val)
                self.adj[root.right.val].add(root.val)
                travesal(root.right)
        travesal(root)
        q = deque()
        q.append([start, 0])
        s = set([start])
        dis = 0
        while q:
            node, dis = q.popleft()
            for i in self.adj[node]:
                if i not in s:
                    q.append([i, dis + 1])
                    s.add(i)
        return dis
    # sử dụng bài tính độ sâu của cây
    # sp dụng vào bài này thì ta được khoảng cách cần tìm = max(độ sâu cây con với root là start, độ sâu của start + độ sâu của nhánh cây còn lại) trong trường hợp start != root
    # trường hợp mà start == root thì chỉ cần trả về độ sâu của cây

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.max_distance = 0  # kết quả bài toán

        def travelsal(root, start):
            depth = 0
            if not root:
                return depth
            # tạo left_depth và right_depth như tìm độ sâu
            left_depth = travelsal(root.left, start)
            right_depth = travelsal(root.right, start)

            if start == root.val:  # trường hợp start == root.val
                self.max_distance = max(left_depth, right_depth)
                depth = -1  # đánh dấu bắt đầu cây có gốc là start
            # nếu cây con chưa hết và không chứa node start thì tiếp tục tăng độ sâu, depth = max(left, right) + 1
            elif left_depth >= 0 and right_depth >= 0:
                depth = max(left_depth, right_depth) + 1
            else:  # cây bên trái hoặc phải chứa start, số âm thể hiện độ sâu của node start
                # khoảng cách sẽ được cập nhật là độ sâu của node start + độ sâu của nhánh còn lại không chứa node start
                distance = abs(left_depth) + abs(right_depth)
                self.max_distance = max(distance, self.max_distance)
                # chưa đến node start thì tiếp tục tăng độ sâu
                depth = min(left_depth, right_depth) - 1
            return depth
        travelsal(root, start)
        return self.max_distance
