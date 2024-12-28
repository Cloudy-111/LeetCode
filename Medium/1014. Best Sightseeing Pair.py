class Solution:
    # Cần tối ưu hóa values[i] + values[j] + i - j
    # biến đổi thành values[i] + i + values[j] - j
    # đặt maxA = values[i] + i
    # tại mỗi bước lặp, tính toán giá trị maxA + values[j] - j và so sánh với kết quả để cập nhật kết quả
    # so sánh maxA với values[j] + j để cập nhật maxA
    #  ý tưởng chính là duy trì kết quả tối ưu tạm thời qua mỗi bước lặp
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxA = values[0]
        res = 0
        for i in range(1, len(values)):
            res = max(res, maxA + values[i] - i)
            maxA = max(maxA, values[i] + i)
        return res
