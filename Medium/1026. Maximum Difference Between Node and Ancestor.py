# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # những bài đệ quy trên cây  nhị phân như này nên tư duy theo kiểu toàn bộ(nhìn vào cách tạo ra kết quả) chứ không nên tư duy cục bộ(quá trình)
    # với bài này, để tìm abs của hiệu node con với node tổ tiên mà lớn nhất thì ta nghĩ theo hướng
    # tìm max, min ở nhánh cây bên trái
    # tìm max, min ở nhánh cây bên phải
    # sau đó tìm maxValue và minValue từ 4 giá trị trên
    # như vậy, ta có thể  tưởng tượng ra  cây  chỉ còn 1 node cha và 2 node con là maxValue và minValue
    # vậy kết quả bài toán sẽ là max giữa abs của hiệu minValue và MaxValue với node cha
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def travesal(root):
            if not root:
                return -10001, 10001  # cây không có node con thì đặt là giới hạn nhỏ nhất và lớn nhất
            # lấy được max và min của cây con trái
            left = travesal(root.left)
            # lấy được max và min của cây con phải
            right = travesal(root.right)

            # tìm được maxValue và minValue, so sánh với chính node đó nếu node đó là lá
            maxValue = max(root.val, max(left[0], right[0]))
            minValue = min(root.val, min(left[1], right[1]))

            # cập nhật  kết quả bài toán
            self.res = max(self.res, abs(root.val - maxValue),
                           abs(root.val - minValue))
            return (maxValue, minValue)  # trả về bộ giá trị max và min
        travesal(root)
        return self.res
