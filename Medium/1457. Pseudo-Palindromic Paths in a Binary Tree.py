# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Cách 1: Duyệt qua tất cả các nhánh và tạo thành 1 path, kiểm tra xem path đó có tổ hợp nào đối xứng hay không
    # nếu path có độ dài lẻ -> có duy nhất 1 số có số lần xuất hiện lẻ, còn lại là chẵn
    # nếu path có độ dài chẵn -> tất cả các số có số lần xuất hiện là chẵn
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dic = defaultdict(int)
        self.len = 0

        def travesal(root):
            self.dic[root.val] += 1
            self.len += 1
            if not root.left and not root.right:
                if self.len % 2 == 0:
                    check = 0
                    for i in self.dic:
                        if self.dic[i] % 2 == 1:
                            check = 1
                            break
                    if check == 0:
                        self.res += 1
                else:
                    cnt = 0
                    for i in self.dic:
                        if self.dic[i] % 2 == 1:
                            cnt += 1
                    if cnt == 1:
                        self.res += 1

            if root.left:
                travesal(root.left)
            if root.right:
                travesal(root.right)
            self.len -= 1
            self.dic[root.val] -= 1
        travesal(root)
        return self.res

    # Cách 2: Sử dụng bitwise, vì đề có đưa ra 1 gợi ý là các node values chỉ nhận các giá trị từ 0 đến 9
    # tạo sẵn mảng có độ dài là 10, nếu mỗi lần gặp số nào thì XOR nó với 1, sau khi kết thúc 1 path thì nếu đối xứng chẵn thì toàn bộ mảng đó nhận giá trị 0
    # nếu path đối xứng lẻ thì chỉ có duy nhất 1 phần tử nhận giá trị 1
    # Thực hiện nhanh và đơn giản hơn cách 1
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.tmp = 0
        self.arr = [0] * 10

        def travesal(root):
            self.arr[root.val] ^= 1
            if not root.left and not root.right:
                self.res += 1 if sum(self.arr) <= 1 else 0

            if root.left:
                travesal(root.left)
            if root.right:
                travesal(root.right)
            self.arr[root.val] ^= 1

        travesal(root)
        return self.res
