# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.s = str(root.val)

        def travesal(root):
            if root.left:
                self.s += '->' + str(root.left.val)
                travesal(root.left)
                self.s = self.s[:-2 - len(str(root.left.val))]
            if root.right:
                self.s += '->' + str(root.right.val)
                travesal(root.right)
                self.s = self.s[:-2 - len(str(root.right.val))]
            if not root.left and not root.right:
                res.append(self.s)
        travesal(root)
        return res
