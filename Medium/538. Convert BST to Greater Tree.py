# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Cách 1: duyệt từ trái sang phải(phải tính được tổng các nút của cây)
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def post(root):
            if not root:
                return 0
            post(root.left)
            self.sum += root.val
            post(root.right)
        post(root)

        def change(root):
            if not root:
                return
            change(root.left)
            self.sum -= root.val
            root.val += self.sum
            change(root.right)
        change(root)
        return root

    # Cách 2: duyệt từ phải sang trái(sẽ thành cộng dồn các nút từ phải sang trái)

    def convertBST(self, root: TreeNode) -> TreeNode:
        def rightToLeft(root, acc):
            if not root:
                return 0
            right = rightToLeft(root.right, acc)
            # giá trị mới = giá trị cũ + nút bên phải nó + giá trị đã tích lũy
            val, root.val = root.val, root.val + acc + right
            left = rightToLeft(root.left, root.val)
            return left + right + val  # tổng giữa nút, nhánh trái, nhánh phải
        rightToLeft(root, 0)
        return root
