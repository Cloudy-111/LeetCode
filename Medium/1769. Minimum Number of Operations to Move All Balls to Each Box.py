class Solution:
    # Ý tưởng đầu tiên: Tìm các vị trí có số 1, lưu các vị trí đó vào 1 mảng
    # Tính tổng khoảng cách từ các vị trí đó đến vị trí hiện tại: abs(j - i)
    # Độ phức tạp là O(n^2)
    def minOperations(self, boxes: str) -> List[int]:
        dis = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                dis.append(i)
        res = [sum(dis)]
        for i in range(1, len(boxes)):
            tmp = 0
            for j in dis:
                j = abs(j - i)
                tmp += j
            res.append(tmp)
        return res


class Solution:
    # Ý tưởng thứ 2: Sử dụng prefixSum để giảm độ phức tạp
    # Nhận thấy nếu vị trí đó là số 0:
    # Tổng lượng chuyển sẽ là tổng lượng chuyển trước đó - số lượng số 1 còn lại + số lượng số 1 đã qua
    # Nếu vị trí đó là số 1:
    # Tổng lượng chuyển sẽ là tổng lượng chuyển trước đó - số lượng số 1 còn lại + số lượng số 1 đã qua - 1(là không tính chính nó)
    # Độ phức tạp là O(n)
    def minOperations(self, boxes: str) -> List[int]:
        num_of_1 = 0
        sum_of_shift_all = 0
        num_of_1_pass = 0
        for idx, char in enumerate(boxes):
            if char == '1':
                num_of_1 += 1
                sum_of_shift_all += idx
        res = [sum_of_shift_all]
        if boxes[0] == '1':
            num_of_1_pass = 1
            num_of_1 -= 1
        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                num_of_1 -= 1
                sum_of_shift_all = sum_of_shift_all - num_of_1 + num_of_1_pass - 1
                num_of_1_pass += 1
            else:
                sum_of_shift_all = sum_of_shift_all - num_of_1 + num_of_1_pass
            res.append(sum_of_shift_all)
        return res
        return res


class Solution:
    # Nhận thấy kí tự đầu tiên là 0 hay 1 thì tổng lượng chuyển đến nó sẽ không thay đổi, có nghĩa là kí tự đầu dùng để xét tổng lượng chuyển đến vị trí thứ 2
    # Suy ra, tổng lượng chuyển đến vị trí thứ i sẽ là tổng lượng chuyển đến vị trí thứ (i - 1) - số lượng số 1 còn lại + số lượng số 1 đã qua
    # Nếu vị trí đó là số 1 thì số lượng số 1 còn lại -1, số lượng số 1 đã qua +1
    def minOperations(self, boxes: str) -> List[int]:
        num_of_1 = 0
        sum_of_shift_all = 0
        num_of_1_pass = 0
        for idx, char in enumerate(boxes):
            if char == '1':
                num_of_1 += 1
                sum_of_shift_all += idx
        res = []
        for i in boxes:
            res.append(sum_of_shift_all)
            if i == '1':
                num_of_1 -= 1
                num_of_1_pass += 1
            sum_of_shift_all = sum_of_shift_all - num_of_1 + num_of_1_pass
        return res
