# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        lv = 0
        currLv = lv
        m = -2**31
        if root is None:
            return []
        q.append((root, lv))
        while q:
            node, lv = q.popleft()
            if currLv != lv:
                res.append(m)
                currLv = lv
                m = max(-2**31, node.val)
            m = max(m, node.val)
            if node.left:
                q.append((node.left, lv + 1))
            if node.right:
                q.append((node.right, lv + 1))
        res.append(m)
        return res
