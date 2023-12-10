# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

# Bài này dùng prefixSum trên mỗi nhánh của cây
# Nếu tổng khi đến node đó trừ đi targetSum mà đã xuất hiện khi tính prefixSum thì tăng biến đếm lên 1(vẽ cây để hiểu rõ hơn)
# từ đó, cần 1 dict để lưu trữ tổng đã tính trên mỗi nhánh, key là tổng đến node đó, value là 1 với những tổng đã đến
# Mỗi nhánh có dict tổng riêng biệt nên sau khi sử dụng xong thì trả lại về 0 để nhánh khác sử dụng

# bài đếm số lượng thì dùng biến tích lũy cnt để tính từ đầu đến cuối và không bị reset


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # tạo dict
        prefixSumMark = defaultdict(int)
        prefixSumMark[0] = 1

        def preorder(root, sum):
            if not root:
                return 0
            # tính prefixsum
            sum += root.val

            # biến đếm sẽ tăng nếu như tổng hiện tại - targetSum đã xuất hiện
            cnt = prefixSumMark[sum - targetSum]

            # đánh dấu tổng hiện tại đã có mặt
            prefixSumMark[sum] += 1

            # đệ quy tiếp để tính
            cnt += preorder(root.left, sum)
            cnt += preorder(root.right, sum)

            # sau khi đã sử dụng xong nhánh đó, trả lại giá trị 0
            prefixSumMark[sum] -= 1
            return cnt
        return preorder(root, 0)
