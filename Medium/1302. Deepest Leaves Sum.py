# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    # Cách 1: tìm độ sâu nhất của cây rồi tính tổng các lá ở tầng sâu nhất
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            return max(left, right) + 1
        self.maxdepth = maxDepth(root)
        self.deepestSum = 0

        def findSum(root, depth):
            if root:
                if self.maxdepth == depth:
                    self.deepestSum += root.val
                findSum(root.left, depth + 1)
                findSum(root.right, depth + 1)
        findSum(root, 1)
        return self.deepestSum

    # Cách 2: duyệt LevelOrder dùng dict
    # mỗi level là 1 list, được lưu vào dic[i]
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)

        def LevelOrder(root, height):
            if not root:
                return
            dic[height].append(root.val)
            LevelOrder(root.left, height + 1)
            LevelOrder(root.right, height + 1)
        LevelOrder(root, 1)
        return sum(dic[len(dic) - 1])

    # Cách 3: Cũng là duyệt LevelOrder nhưng không cần thiết phải lưu lại các level trước
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        while level:
            tempLevel = level
            level = []
            for i in tempLevel:
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
        return sum([i.val for i in tempLevel])
