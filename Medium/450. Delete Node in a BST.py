# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def leftNodeMost(root):
            while root.left:
                root = root.left
            return root.val

        if not root:
            return
        # tìm kiếm node cần xóa
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        if root.val == key: # đã tìm thấy node
            # có 3 trường hợp: 
            # nó là node lá(không có con) -> không trả về gì cả(không thực hiện (return))
            # nó có 1 node con -> trả về node đó luôn
            # nó còn 2 node con, là node trung gian -> tìm phần tử con trái nhất của cây bên phải nó, thay thế nó bằng phần tử vừa tìm được, xóa phần tử đó đi 
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = leftNodeMost(root.right)
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)
        return root
