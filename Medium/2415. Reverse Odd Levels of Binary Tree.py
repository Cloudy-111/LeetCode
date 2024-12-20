from collections import deque

# Definition for a binary tree node.
# Ý tưởng bài này không có gì nhiều: DFS hay BFS cũng dùng được
# VỚi BFS: duyệt theo mức, nếu mức là số lẻ thì đảo ngược giá trị của node
# Với DFS: nếu mức đó là mức lẻ thì swap 2 node con của node đó


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append((root, 0))
        s = []
        while q:
            node, lv = q.popleft()
            if lv % 2 == 1:
                s.append(node)
            elif s:
                self.process(s)
                s = []
            if node.left:
                q.append((node.left, lv + 1))
            if node.right:
                q.append((node.right, lv + 1))
        if s:
            self.process(s)
        return root

    def process(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            s[i].val, s[j].val = s[j].val, s[i].val
            i += 1
            j -= 1

# DFS


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.travesal(root.left, root.right, 0)
        return root

    def travesal(self, left, right, lv):
        if not left or not right:
            return
        if lv % 2 == 1:
            left.val, right.val = right.val, left.val
        self.travesal(left.left, right.right, lv + 1)
        self.travesal(left.right, right.left, lv + 1)
