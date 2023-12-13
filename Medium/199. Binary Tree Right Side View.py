# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            deq = [root]
            while deq:
                res.append(deq[-1].val)
                tmp = deq
                deq = []
                for i in tmp:
                    if i.left:
                        deq.append(i.left)
                    if i.right:
                        deq.append(i.right)
        return res
