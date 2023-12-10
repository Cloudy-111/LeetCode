# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bài này dùng biến tích lũy có reset khi không đổi hướng(step) nên biến đó được đưa luôn vào trong các tham số của hàm

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # quan trọng là phải có max length để theo dõi số bước
        self.maxLength = 0

        def DFS(root, direct, step):
            if root:
                self.maxLength = max(self.maxLength, step)
                if direct == 1:  # nếu hướng trước đó là phải thì bước sang trái sẽ có số bước + thêm 1, bước sang phải thì số bước sẽ reset về 1
                    DFS(root.left, -1, step + 1)
                    DFS(root.right, 1, 1)
                else:  # nếu hướng trước đó là trái thì bước sang phải sẽ có số bước + thêm 1, bước sang trái thì số bước sẽ reset về 1
                    DFS(root.right, 1, step + 1)
                    DFS(root.left, -1, 1)

        DFS(root, -1, 0)  # đi sang trái, gắn số bước = 0
        DFS(root, 1, 0)  # đi sang phải, gắn số bước = 0
        return self.maxLength
