# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # mấu chốt là tìm xem  cây bên trái có xuất hiện p hay không, cây bên phải có xuất hiện q hay không
    # nếu cây bên trái có p và cây bên phải có q thì trả về root
    # nếu cây bên trái có p mà cây bên phải không có q thì trả về p và ngược lại
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or q.val == root.val:
            return root
        left_LCA = self.lowestCommonAncestor(root.left, p, q)
        right_LCA = self.lowestCommonAncestor(root.right, p, q)

        if left_LCA and right_LCA:
            return root
        return left_LCA if left_LCA else right_LCA
