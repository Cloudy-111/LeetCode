class Solution:
    # Đọc đề kĩ kẻo ngộ nhận: Đề bài cho là robot thứ 1 đi sao cho robot thứ 2 lấy điểm là nhỏ nhất, robot2 đi lấy số điểm lớn nhất còn lại
    # Có nghĩa là robot 1 sẽ chọn đường đi sao cho tổng điểm của robot 2 là nhỏ nhất chứ không phải robot1 đi sao cho điểm robot1 lấy là nhiều nhất
    # Vì mảng chỉ có 2 hàng, sau khi robot1 đi xong, phần còn lại để robot2 đi sẽ là 1 loạt các ô khác 0 ở nửa cuối hàng 1 và nửa đầu hàng 2, tại chỉ số mà robot1 chuyển xướng hàng dưới thì cả 2 hàng là 0 0
    # Như vậy robot2 nếu muốn có điểm lớn nhất thì sẽ chỉ chọn được 1 trong 2 hàng để đi -> cần cân bằng điểm ở nửa đầu hàng 2 và nửa cuối hàng 1
    # Với mỗi lần duyệt i từ 1 đến len(grid[0]) có nghĩa là tại i robot1 chuyển hàng, robot2 sẽ chọn max giữa số điểm từ i + 1 đến cuối hàng 1 và từ đầu hàng 2 đến i - 1
    # Và để robot2 lấy được ít điểm nhất thì robot1 sẽ min trong tất cả trường hợp trên
    def gridGame(self, grid: List[List[int]]) -> int:
        # Số điểm còn lại của hàng 1 nếu robot1 chuyển hàng
        up = sum(grid[0]) - grid[0][0]
        down = 0  # Số điểm hàng 2 có được nếu robot1 chuyển hàng
        m = len(grid[0])
        optimize = [max(up, down)]
        for i in range(1, m):  # Duyệt qua các trường hợp robot1 chuyển hàng
            up -= grid[0][i]
            down += grid[1][i - 1]
            optimize.append(max(up, down))
        return min(optimize)
