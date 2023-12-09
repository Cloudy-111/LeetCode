# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafList(root, lst):
            if root:
                if not root.left and not root.right:
                    lst.append(root.val)
                else:
                    leafList(root.left, lst)
                    leafList(root.right, lst)
        lst1 = []
        lst2 = []
        leafList(root1, lst1)
        leafList(root2, lst2)
        return lst1 == lst2
