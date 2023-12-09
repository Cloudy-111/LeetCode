# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxCurr = root.val

        def preorder(maxCurr, root):
            if not root:
                return 0
            res = 0
            if maxCurr <= root.val:
                res += 1
                maxCurr = root.val
            res += preorder(maxCurr, root.left)
            res += preorder(maxCurr, root.right)
            return res

        return preorder(maxCurr, root)
