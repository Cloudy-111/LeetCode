# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  # Trả về một tham chiếu tới cùng một nút trong cây cloned.

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def Travesal(original, cloned):
            if original:
                Travesal(original.left, cloned.left)
                # Với cây không chứa các nút có giá trị giống nhau
                # thì có thể so sánh trực tiếp giá trị
                # original.val == cloned.val
                # Với cây chứa các nút có giá trị giống nhau
                if original is target:
                    self.res = cloned
                Travesal(original.right, cloned.right)
        Travesal(original, cloned)
        return self.res
