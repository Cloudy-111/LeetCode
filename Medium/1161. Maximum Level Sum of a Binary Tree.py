# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # tạo ra 1 mảng gồm các tổng của các level rồi so sánh từng tổng một
    # nhưng mà bị cái là duyệt qua mỗi node tận 2 lần, 1 lần để xác định chiều cao của cây, 1 lần để duyệt queue
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            left = height(root.left) + 1
            right = height(root.right) + 1
            return max(left, right)
        h = height(root)  # O(n)
        queue = []
        sumOfLevel = [0] * (h + 1)
        queue.append([root, 1])
        while len(queue) > 0:  # O(n)
            t, l = queue.pop(0)
            sumOfLevel[l] += t.val
            if t.left:
                queue.append([t.left, l + 1])
            if t.right:
                queue.append([t.right, l + 1])
        m = max(sumOfLevel[1:])
        for i in range(1, h + 1):
            if sumOfLevel[i] == m:
                return i

    # mỗi node duyệt qua 1 lần, chỉ cần biết tổng tầng hiện tại và max, không cần biết các tổng trước đó là gì -> không cần lưu vào mảng
    # khôngg cần biết những tầng trước đó, chỉ cần xét tầng hiện tại
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxSum = float('-inf')
        maxLevel = 1
        level = 1
        queue = [root]
        while queue:
            levelSum = 0
            nextLevel = []
            for i in queue:
                levelSum += i.val
                if i.left:
                    nextLevel.append(i.left)
                if i.right:
                    nextLevel.append(i.right)
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
            level += 1
            queue = nextLevel
        return maxLevel
