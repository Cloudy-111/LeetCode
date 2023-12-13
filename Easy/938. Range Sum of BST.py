# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0

        def BSTTravesal(root, low, high):
            if not root:
                return
            if root.val >= low and root.val <= high:
                self.result += root.val
            else:
                return
            BSTTravesal(root.left, low, high)
            BSTTravesal(root.right, low, high)
        BSTTravesal(root, low, high)
        return self.result
