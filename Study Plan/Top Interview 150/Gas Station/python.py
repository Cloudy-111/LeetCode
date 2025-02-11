class Solution:
    # Nếu tổng cost mà lớn hơn tổng gas thì chắc chắn không thể chọn bất cứ trạm nào để xuất phát cả
    # Những trường hợp còn lại thì chắc chắn sẽ có thể chọn được trạm xuất phát
    # ta sử dụng biến current để theo dõi lượng gas còn lại của xe
    # Nếu current mà < 0 khi đến trạm đó thì ta sẽ lấy trạm đó làm điểm xuất phát tiếp theo
    # và cập nhật current = gas[i] (lượng gas còn lại của xe)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        res = 0
        current = gas[0]  # đặt điểm xuất phát là trạm đầu tiên
        for i in range(1, len(gas)):
            current = current - cost[i - 1]
            if current < 0:
                res = i
                current = gas[i]
            else:
                current += gas[i]
        return res
